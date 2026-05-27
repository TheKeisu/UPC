from __future__ import annotations

import json
from pathlib import Path

from core.custom.solver import get_formula_symbols


BASE_DIR = Path(__file__).resolve().parent
STORE_PATH = BASE_DIR / "formulas.json"


def _normalize_variable(variable: dict) -> dict:
    if not isinstance(variable, dict):
        raise ValueError("Каждая величина должна быть объектом")

    name = str(variable.get("name") or "").strip()
    unit_symbol = str(variable.get("unit_symbol") or "").strip()

    if not name or not unit_symbol:
        raise ValueError("Каждая величина должна содержать name и unit_symbol")

    return {
        "name": name,
        "unit_symbol": unit_symbol,
    }


def _normalize_result(result: dict | None) -> dict | None:
    if result is None:
        return None
    if not isinstance(result, dict):
        raise ValueError("Поле result должно быть объектом")

    display_name = str(result.get("display_name") or "Результат").strip()
    unit_symbol = str(result.get("unit_symbol") or "").strip()

    return {
        "display_name": display_name or "Результат",
        "unit_symbol": unit_symbol,
    }


def _reconcile_variables(
    formula: str,
    variables: list[dict],
    *,
    strict: bool,
) -> list[dict]:
    symbols = get_formula_symbols(formula)
    exact_variables_by_name: dict[str, dict] = {}
    lower_variables_by_name: dict[str, list[dict]] = {}
    for item in variables:
        name = str(item.get("name") or "").strip()
        if not name:
            continue

        normalized = _normalize_variable(item)
        exact_variables_by_name[name] = normalized
        lower_variables_by_name.setdefault(name.lower(), []).append(normalized)

    ordered_variables: list[dict] = []
    missing_symbols: list[str] = []
    for symbol in symbols:
        variable = exact_variables_by_name.get(symbol)
        if variable is None:
            candidates = lower_variables_by_name.get(symbol.lower(), [])
            if len(candidates) == 1:
                variable = candidates[0]
        if variable is None:
            if strict:
                missing_symbols.append(symbol)
                continue
            variable = {"name": symbol, "unit_symbol": ""}
        ordered_variables.append(variable)

    if missing_symbols:
        missing = ", ".join(missing_symbols)
        raise ValueError(f"Для символов {missing} не описаны величины")

    if strict:
        extras = [
            item["name"]
            for name, item in exact_variables_by_name.items()
            if name not in symbols and name.lower() not in {symbol.lower() for symbol in symbols}
        ]
        if extras:
            extra_names = ", ".join(extras)
            raise ValueError(f"Указаны лишние величины: {extra_names}")

    return ordered_variables


def _build_description(variables: list[dict], result: dict | None) -> str:
    variables_line = "; ".join(
        f"{item['name']} ({item['unit_symbol']})" if item.get("unit_symbol") else item["name"]
        for item in variables
    )
    if result is None:
        return f"Величины: {variables_line}"

    result_unit = str(result.get("unit_symbol") or "").strip()
    result_line = f"Результат: {result['display_name']}"
    if result_unit:
        result_line += f" ({result_unit})"

    return f"Величины: {variables_line}. {result_line}"


def _build_formula_entry(
    index: int,
    title: str,
    variables: list[dict],
    formula: str,
    result: dict | None = None,
) -> dict:
    entry = {
        "id": f"custom_{index}",
        "title": title,
        "variables": variables,
        "formula": formula,
        "description": _build_description(variables, result),
        "formula_view": formula,
    }
    if result is not None:
        entry["result"] = result
    return entry


def _normalize_formula(raw: dict, index: int) -> dict:
    title = str(raw.get("title") or f"Пользовательская формула {index}").strip()
    formula = str(raw.get("formula") or "").strip()
    if not formula:
        raise ValueError("Поле formula не может быть пустым")

    variables_raw = raw.get("variables")
    if not isinstance(variables_raw, list):
        raise ValueError("Поле variables должно быть списком")

    variables = _reconcile_variables(formula, variables_raw, strict=False)

    result = _normalize_result(raw.get("result"))

    return _build_formula_entry(
        index=index,
        title=title,
        variables=variables,
        formula=formula,
        result=result,
    )


def _normalize_payload(payload: dict) -> dict:
    formulas_raw = payload.get("formulas")
    if not isinstance(formulas_raw, list):
        raise ValueError("Корневое поле formulas должно быть списком")

    formulas: list[dict] = []
    for index, raw_formula in enumerate(formulas_raw, start=1):
        if not isinstance(raw_formula, dict):
            raise ValueError("Каждая формула должна быть объектом")
        formulas.append(_normalize_formula(raw_formula, index))

    return {"formulas": formulas}


def _read_payload() -> dict:
    if not STORE_PATH.exists():
        return {"formulas": []}

    try:
        with STORE_PATH.open("r", encoding="utf-8") as stream:
            payload = json.load(stream)
    except (json.JSONDecodeError, OSError):
        return {"formulas": []}

    formulas = payload.get("formulas")
    if not isinstance(formulas, list):
        return {"formulas": []}
    return {"formulas": formulas}


def _write_payload(payload: dict) -> None:
    STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with STORE_PATH.open("w", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)


def list_custom_formulas() -> list[dict]:
    payload = _read_payload()
    formulas: list[dict] = []
    for index, item in enumerate(payload["formulas"], start=1):
        try:
            formulas.append(_normalize_formula(item, index))
        except ValueError:
            continue
    return formulas


def add_custom_formula(
    title: str,
    variables: list[dict],
    formula: str,
    result: dict | None = None,
) -> str:
    payload = _read_payload()
    formulas = payload["formulas"]

    formula_id = f"custom_{len(formulas) + 1}"
    formulas.append(
        _build_formula_entry(
            index=len(formulas) + 1,
            title=title,
            variables=_reconcile_variables(formula, variables, strict=True),
            formula=formula,
            result=_normalize_result(result),
        )
    )

    _write_payload(payload)
    return formula_id


def export_custom_formulas(target_path: str) -> str:
    payload = {"formulas": list_custom_formulas()}
    destination = Path(target_path).expanduser()
    if destination.suffix.lower() != ".json":
        destination = destination.with_suffix(".json")

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
    return str(destination)


def import_custom_formulas(source_path: str) -> int:
    source = Path(source_path).expanduser()
    if not source.exists():
        raise FileNotFoundError("Файл для импорта не найден")

    with source.open("r", encoding="utf-8") as stream:
        payload = json.load(stream)

    normalized = _normalize_payload(payload)
    _write_payload(normalized)
    return len(normalized["formulas"])


def as_registry_map() -> dict:
    result = {}
    for item in list_custom_formulas():
        formula_id = item.get("id")
        if not formula_id:
            continue

        result[formula_id] = {
            "title": item.get("title", "Пользовательская формула"),
            "description": item.get("description", ""),
            "formula_view": item.get("formula_view") or item.get("formula", ""),
        }
    return result
