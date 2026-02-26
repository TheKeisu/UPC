from __future__ import annotations

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
STORE_PATH = BASE_DIR / "formulas.json"


def _build_formula_entry(index: int, title: str, variables: list[dict], formula: str) -> dict:
    variables_line = ", ".join(
        f"{item['name']} ({item['unit_symbol']})" for item in variables
    )
    return {
        "id": f"custom_{index}",
        "title": title,
        "variables": variables,
        "formula": formula,
        "description": f"Величины: {variables_line}",
        "formula_view": formula,
    }


def _normalize_formula(raw: dict, index: int) -> dict:
    title = str(raw.get("title") or f"Пользовательская формула {index}").strip()
    formula = str(raw.get("formula") or "").strip()
    if not formula:
        raise ValueError("Поле formula не может быть пустым")

    variables_raw = raw.get("variables")
    if not isinstance(variables_raw, list):
        raise ValueError("Поле variables должно быть списком")

    variables: list[dict] = []
    for variable in variables_raw:
        if not isinstance(variable, dict):
            raise ValueError("Каждая величина должна быть объектом")
        name = str(variable.get("name") or "").strip()
        unit_symbol = str(variable.get("unit_symbol") or "").strip()
        if not name or not unit_symbol:
            raise ValueError("Каждая величина должна содержать name и unit_symbol")
        variables.append({"name": name, "unit_symbol": unit_symbol})

    return _build_formula_entry(index=index, title=title, variables=variables, formula=formula)


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
    return payload["formulas"]


def add_custom_formula(title: str, variables: list[dict], formula: str) -> str:
    payload = _read_payload()
    formulas = payload["formulas"]

    formula_id = f"custom_{len(formulas) + 1}"
    formulas.append(
        _build_formula_entry(
            index=len(formulas) + 1,
            title=title,
            variables=variables,
            formula=formula,
        )
    )

    _write_payload(payload)
    return formula_id


def export_custom_formulas(target_path: str) -> str:
    payload = _read_payload()
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
