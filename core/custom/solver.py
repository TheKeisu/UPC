from __future__ import annotations

from sympy import Eq, Symbol, solve, sympify


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
    target_symbol = all_symbols.get(target_variable)
    if target_symbol is None:
        target_symbol = all_symbols.get(target_variable.lower())
    if target_symbol is None:
        for name, symbol in all_symbols.items():
            if name.lower() == target_variable.lower():
                target_symbol = symbol
                break
    if target_symbol is None:
        target_symbol = Symbol(target_variable)

    raw_solutions = solve(substituted, target_symbol)

    solutions: list[float] = []
    for value in raw_solutions:
        if getattr(value, "free_symbols", None):
            continue
        solutions.append(float(value.evalf()))

    return solutions
