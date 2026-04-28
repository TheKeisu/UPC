from __future__ import annotations

from sympy import Eq, Symbol, solve, sympify


def _format_number(value: float) -> str:
    return f"{value:.10g}"


def _build_metadata_map(items: list[dict] | None) -> dict[str, dict]:
    metadata_map: dict[str, dict] = {}
    metadata_map_lower: dict[str, dict] = {}
    for item in items or []:
        name = str(item.get("name") or "").strip()
        if not name:
            continue

        unit_symbol = str(item.get("unit_symbol") or "").strip()
        display_name = str(item.get("display_name") or "").strip()
        metadata = {
            "name": name,
            "display_name": display_name or name,
            "unit_symbol": unit_symbol,
        }
        metadata_map[name] = metadata
        metadata_map_lower.setdefault(name.lower(), metadata)

    return {**metadata_map_lower, **metadata_map}


def _normalize_result_metadata(result: dict | None) -> dict:
    if not result:
        return {
            "display_name": "Результат",
            "unit_symbol": "",
        }

    unit_symbol = str(result.get("unit_symbol") or "").strip()
    return {
        "display_name": str(result.get("display_name") or "Результат").strip() or "Результат",
        "unit_symbol": unit_symbol,
    }


def _get_metadata(name: str, metadata_map: dict[str, dict]) -> dict:
    metadata = metadata_map.get(name)
    if metadata is None:
        metadata = metadata_map.get(name.lower())
    if metadata is not None:
        return metadata

    return {
        "name": name,
        "unit_symbol": "",
    }


def _format_quantity(metadata: dict) -> str:
    return metadata.get("display_name") or metadata.get("name") or "Результат"


def _format_unit(metadata: dict) -> str:
    return str(metadata.get("unit_symbol") or "").strip()


def _format_value_with_unit(value: float, metadata: dict) -> str:
    unit = _format_unit(metadata)
    if unit:
        return f"{_format_number(value)} {unit}"
    return _format_number(value)


def _format_known_values(known_values: dict[str, float], metadata_map: dict[str, dict]) -> str:
    parts: list[str] = []
    for key, value in known_values.items():
        metadata = _get_metadata(key, metadata_map)
        parts.append(f"{_format_quantity(metadata)} = {_format_value_with_unit(value, metadata)}")
    return "; ".join(parts)


def _resolve_target_symbol(target_variable: str, symbol_map: dict[str, Symbol]) -> Symbol:
    target_symbol = symbol_map.get(target_variable)
    if target_symbol is None:
        target_symbol = symbol_map.get(target_variable.lower())
    if target_symbol is None:
        for name, symbol in symbol_map.items():
            if name.lower() == target_variable.lower():
                target_symbol = symbol
                break
    if target_symbol is None:
        target_symbol = Symbol(target_variable)
    return target_symbol


def get_formula_symbols(formula: str) -> list[str]:
    if "=" in formula:
        left, right = formula.split("=", 1)
        expression = sympify(left) - sympify(right)
    else:
        expression = sympify(formula)

    return sorted(symbol.name for symbol in expression.free_symbols)


def _build_substitutions(expression, known_values: dict[str, float]) -> dict:
    symbols_by_name = {symbol.name: symbol for symbol in expression.free_symbols}
    symbols_by_lower = {name.lower(): symbol for name, symbol in symbols_by_name.items()}

    substitutions = {}
    for key, value in known_values.items():
        symbol = symbols_by_name.get(key)
        if symbol is None:
            symbol = symbols_by_lower.get(key.lower())
        if symbol is not None:
            substitutions[symbol] = value

    return substitutions


def eval_expression(formula: str, known_values: dict[str, float]) -> float:
    expression = sympify(formula)
    substitutions = _build_substitutions(expression, known_values)
    result = expression.subs(substitutions)

    if result.free_symbols:
        missing = ", ".join(sorted(symbol.name for symbol in result.free_symbols))
        raise ValueError(f"Не заданы значения для: {missing}")

    return float(result.evalf())


def solve_equation(formula: str, target_variable: str, known_values: dict[str, float]) -> list[float]:
    if "=" not in formula:
        raise ValueError("Формула не является уравнением")

    left, right = formula.split("=", 1)
    equation = Eq(sympify(left), sympify(right))

    substitutions = _build_substitutions(equation.lhs - equation.rhs, known_values)
    substituted = equation.subs(substitutions)

    all_symbols = {symbol.name: symbol for symbol in (equation.lhs - equation.rhs).free_symbols}
    target_symbol = _resolve_target_symbol(target_variable, all_symbols)

    raw_solutions = solve(substituted, target_symbol)

    solutions: list[float] = []
    for value in raw_solutions:
        if getattr(value, "free_symbols", None):
            continue
        solutions.append(float(value.evalf()))

    return solutions


def solve_formula_with_steps(
    formula: str,
    known_values: dict[str, float],
    *,
    target_variable: str | None = None,
    variables: list[dict] | None = None,
    result: dict | None = None,
) -> dict:
    variables_map = _build_metadata_map(variables)
    known_values_text = _format_known_values(known_values, variables_map)

    if "=" in formula:
        if not target_variable:
            raise ValueError("Для уравнения нужно указать искомую величину")

        left, right = formula.split("=", 1)
        equation = Eq(sympify(left), sympify(right))
        expression = equation.lhs - equation.rhs
        substitutions = _build_substitutions(expression, known_values)
        substituted = equation.subs(substitutions)

        all_symbols = {symbol.name: symbol for symbol in expression.free_symbols}
        target_symbol = _resolve_target_symbol(target_variable, all_symbols)
        target_metadata = _get_metadata(target_symbol.name, variables_map)

        raw_solutions = solve(substituted, target_symbol)
        numeric_solutions: list[float] = []
        rendered_solutions: list[str] = []

        for value in raw_solutions:
            if getattr(value, "free_symbols", None):
                continue
            numeric_value = float(value.evalf())
            numeric_solutions.append(numeric_value)
            rendered_solutions.append(f"{target_symbol} = {_format_number(numeric_value)}")

        if not numeric_solutions:
            raise ValueError("Не удалось получить численное решение")

        steps = [
            f"1. Исходная формула: {equation.lhs} = {equation.rhs}",
            f"2. Ищем: {_format_quantity(target_metadata)}",
        ]

        if known_values_text:
            steps.append(f"3. Известные значения: {known_values_text}")
            steps.append(f"4. После подстановки: {substituted.lhs} = {substituted.rhs}")
            steps.append(
                f"5. Выражаем {target_symbol}: {'; '.join(rendered_solutions)}"
            )
            answer_index = 6
        else:
            steps.append(
                f"3. Выражаем {target_symbol}: {'; '.join(rendered_solutions)}"
            )
            answer_index = 4

        if len(numeric_solutions) == 1:
            answer_text = (
                f"{_format_quantity(target_metadata)} = "
                f"{_format_value_with_unit(numeric_solutions[0], target_metadata)}"
            )
        else:
            answer_text = ", ".join(
                _format_value_with_unit(value, target_metadata)
                for value in numeric_solutions
            )
            answer_text = f"Возможные значения {_format_quantity(target_metadata)}: {answer_text}"

        steps.append(f"{answer_index}. Ответ: {answer_text}")
        return {
            "mode": "equation",
            "target": target_symbol.name,
            "target_metadata": target_metadata,
            "solutions": numeric_solutions,
            "steps": steps,
            "answer": answer_text,
        }

    expression = sympify(formula)
    substitutions = _build_substitutions(expression, known_values)
    substituted = expression.subs(substitutions)

    if substituted.free_symbols:
        missing = ", ".join(sorted(symbol.name for symbol in substituted.free_symbols))
        raise ValueError(f"Не заданы значения для: {missing}")

    numeric_result = float(substituted.evalf())
    result_metadata = _normalize_result_metadata(result)

    steps = [
        f"1. Исходное выражение: {expression}",
        f"2. Ищем: {_format_quantity(result_metadata)}",
    ]

    if known_values_text:
        steps.append(f"3. Известные значения: {known_values_text}")
        steps.append(f"4. После подстановки: {substituted}")
        answer_index = 5
    else:
        answer_index = 3

    answer_text = (
        f"{_format_quantity(result_metadata)} = "
        f"{_format_value_with_unit(numeric_result, result_metadata)}"
    )
    steps.append(f"{answer_index}. Ответ: {answer_text}")

    return {
        "mode": "expression",
            "target": result_metadata["display_name"],
        "target_metadata": result_metadata,
        "value": numeric_result,
        "steps": steps,
        "answer": answer_text,
    }
