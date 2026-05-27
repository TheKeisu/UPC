from __future__ import annotations

from copy import deepcopy

from core.custom.solver import solve_formula_with_steps
from .formulas import SECTIONS


def _read_float(prompt: str) -> float:
    return float(input(prompt).strip().replace(",", "."))


def _print_steps(steps: list[str]) -> None:
    print("Пошаговое решение:")
    for step in steps:
        print(step)


def _prepare_formula_payload(formula: str, variables: list[dict]) -> tuple[str, list[dict]]:
    prepared_formula = formula.lower()
    prepared_variables = deepcopy(variables)

    for item in prepared_variables:
        original_name = str(item.get("name") or "").strip()
        item["display_name"] = original_name
        item["name"] = original_name.lower()

    return prepared_formula, prepared_variables


def run_handbook_console() -> None:
    section_names = list(SECTIONS.keys())
    print("Разделы математики:")
    for i, section_name in enumerate(section_names, start=1):
        print(f"{i}. {section_name}")

    section_index = int(input("Выберите раздел математики: ")) - 1
    if section_index < 0 or section_index >= len(section_names):
        print("Неверный раздел")
        return

    section_name = section_names[section_index]
    formulas = SECTIONS[section_name]

    print(f"Формулы раздела '{section_name}':")
    for i, item in enumerate(formulas, start=1):
        print(f"{i}. {item['title']} -> {item['formula']}")

    formula_index = int(input("Выберите формулу: ")) - 1
    if formula_index < 0 or formula_index >= len(formulas):
        print("Неверная формула")
        return

    selected = formulas[formula_index]
    formula = selected["formula"]
    variables = selected["variables"]
    prepared_formula, prepared_variables = _prepare_formula_payload(formula, variables)

    print("Доступные величины:")
    for variable in prepared_variables:
        unit = str(variable.get("unit_symbol") or "").strip()
        suffix = f" ({unit})" if unit else ""
        print(f"- {variable.get('display_name', variable['name'])}{suffix}")

    target_variable_input = input("Что найти (обозначение): ").strip()
    target_variable = target_variable_input.lower()
    variable_names = {str(item.get("name") or "").strip() for item in prepared_variables}
    if target_variable not in variable_names:
        print("Неизвестная величина")
        return

    known_values: dict[str, float] = {}
    for variable in prepared_variables:
        name = str(variable.get("name") or "").strip()
        if name == target_variable:
            continue
        display_name = str(variable.get("display_name") or name)
        known_values[name] = _read_float(f"Введите {display_name}: ")

    try:
        solution = solve_formula_with_steps(
            prepared_formula,
            known_values,
            target_variable=target_variable,
            variables=prepared_variables,
        )
    except (TypeError, ValueError, ZeroDivisionError) as error:
        print(f"Ошибка вычисления: {error}")
        return

    _print_steps(solution["steps"])
