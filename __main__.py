from core.common.sections import section_selection
from core.common.sections import sections
import sys


def _read_float(prompt: str) -> float:
    value = input(prompt).strip().replace(",", ".")
    return float(value)


def _format_unit_text(item: dict) -> str:
    return str(item.get("unit_symbol") or "").strip()


def _format_quantity_text(item: dict) -> str:
    symbol = str(item.get("name") or "").strip()
    unit = _format_unit_text(item)

    if unit:
        return f"{symbol} ({unit})"
    return symbol


def _find_variable_by_alias(variables: list[dict], alias: str) -> dict | None:
    alias_normalized = alias.strip().lower()
    for item in variables:
        name = str(item.get("name") or "").strip().lower()
        if alias_normalized == name:
            return item
    return None


def run_console_physics() -> None:
    section = int(
        input(
            "Выберите раздел физики "
            "(Механика - 1 ;"
            " Термодинамика и статистическая физика - 2 ;"
            " Электродинамика - 3 ;"
            " Оптика - 4;)"
        )
    )

    section_selection(sections[section], section)


def run_console_math() -> None:
    from core.math.handbook import run_handbook_console

    run_handbook_console()


def run_console_custom() -> None:
    from core.custom.formula_store import (
        add_custom_formula,
        list_custom_formulas,
        export_custom_formulas,
        import_custom_formulas,
    )
    from core.custom.solver import solve_formula_with_steps

    action = int(
        input(
            "Свои формулы: "
            "(Добавить формулу - 1;"
            " Показать список - 2;"
            " Использовать формулу - 3;"
            " Экспорт JSON - 4;"
            " Импорт JSON - 5;)"
        )
    )

    if action == 2:
        formulas = list_custom_formulas()
        if not formulas:
            print("Пользовательских формул пока нет")
            return

        for item in formulas:
            print(f"- {item.get('title', 'Пользовательская формула')}: {item.get('formula', '')}")
            for variable in item.get("variables", []):
                print(f"    • {_format_quantity_text(variable)}")
            result = item.get("result")
            if result:
                result_name = str(result.get("display_name") or "Результат").strip()
                result_unit = _format_unit_text(result)
                suffix = f" ({result_unit})" if result_unit else ""
                print(f"    • Результат: {result_name}{suffix}")
        return

    if action == 3:
        formulas = list_custom_formulas()
        if not formulas:
            print("Пользовательских формул пока нет")
            return

        print("Выберите формулу:")
        for index, item in enumerate(formulas, start=1):
            print(f"{index}. {item.get('title', 'Пользовательская формула')}: {item.get('formula', '')}")

        selected_index = int(input("Номер формулы: ")) - 1
        if selected_index < 0 or selected_index >= len(formulas):
            print("Неверный номер формулы")
            return

        selected_formula = formulas[selected_index]
        formula_text = selected_formula.get("formula", "").strip()
        variables = selected_formula.get("variables", [])

        if not formula_text:
            print("У выбранной формулы нет выражения")
            return

        if "=" in formula_text:
            print("Доступные величины:")
            for variable in variables:
                print(f"- {_format_quantity_text(variable)}")

            target_input = input("Что найти (обозначение): ").strip()
            target_variable = _find_variable_by_alias(variables, target_input)
            if target_variable is None:
                print("Неизвестная величина")
                return

            known_values: dict[str, float] = {}
            for variable in variables:
                variable_name = str(variable.get("name") or "").strip()
                if variable_name.lower() == str(target_variable.get("name") or "").strip().lower():
                    continue
                known_values[variable_name] = _read_float(
                    f"Введите {_format_quantity_text(variable)}: "
                )

            try:
                solution = solve_formula_with_steps(
                    formula_text,
                    known_values,
                    target_variable=str(target_variable.get("name") or "").strip(),
                    variables=variables,
                )
            except (TypeError, ValueError) as error:
                print(f"Ошибка вычисления: {error}")
                return

            print("Пошаговое решение:")
            for step in solution["steps"]:
                print(step)
            return

        known_values: dict[str, float] = {}
        for variable in variables:
            variable_name = str(variable.get("name") or "").strip()
            known_values[variable_name] = _read_float(
                f"Введите {_format_quantity_text(variable)}: "
            )

        try:
            solution = solve_formula_with_steps(
                formula_text,
                known_values,
                variables=variables,
                result=selected_formula.get("result"),
            )
        except (TypeError, ValueError) as error:
            print(f"Ошибка вычисления: {error}")
            return

        print("Пошаговое решение:")
        for step in solution["steps"]:
            print(step)
        return

    if action == 4:
        target_path = input("Путь для экспорта (.json): ").strip()
        if not target_path:
            print("Путь не может быть пустым")
            return

        try:
            exported_to = export_custom_formulas(target_path)
        except OSError as error:
            print(f"Ошибка экспорта: {error}")
            return

        print(f"Экспорт завершён: {exported_to}")
        return

    if action == 5:
        source_path = input("Путь к JSON для импорта: ").strip()
        if not source_path:
            print("Путь не может быть пустым")
            return

        try:
            imported_count = import_custom_formulas(source_path)
        except (OSError, ValueError, FileNotFoundError) as error:
            print(f"Ошибка импорта: {error}")
            return

        print(f"Импорт завершён. Загружено формул: {imported_count}")
        return

    if action != 1:
        print("Неизвестное действие")
        return

    next_number = len(list_custom_formulas()) + 1
    entered_title = input("Введите название формулы (можно оставить пустым): ").strip()
    title = entered_title or f"Пользовательская формула {next_number}"

    count = int(input("Шаг 1. Введите количество величин: "))
    if count <= 0:
        print("Количество должно быть больше нуля")
        return

    variables = []
    for index in range(1, count + 1):
        name = input(f"Шаг 2. Обозначение величины {index}: ").strip()
        unit = input(f"Шаг 2. Обозначение единицы для величины {index}: ").strip()
        if not name or not unit:
            print("Обозначение величины и обозначение единицы обязательны")
            return
        variables.append(
            {
                "name": name,
                "unit_symbol": unit,
            }
        )

    formula = input("Шаг 3. Введите формулу: ").strip()
    if not formula:
        print("Формула не может быть пустой")
        return

    result = None
    if "=" not in formula:
        result_name = input("Шаг 4. Название искомой величины: ").strip()
        result_unit = input("Шаг 4. Обозначение единицы искомой величины: ").strip()

        if not result_name:
            print("Название искомой величины обязательно")
            return

        result = {
            "display_name": result_name,
            "unit_symbol": result_unit,
        }

    add_custom_formula(title=title, variables=variables, formula=formula, result=result)
    print("Формула сохранена")


def run_console_chemistry() -> None:
    from core.chemistry.periodic_table import run_console_chemistry as periodic_table_console
    from core.chemistry.general.solver import formula_selection as chemistry_formula_selection
    from core.chemistry.general.enum import GENERAL_CHEMISTRY, REACTION_STOICHIOMETRY

    action = int(
        input(
            "Химия: "
            "(Формулы и вычисления - 1; "
            "Таблица Менделеева - 2; "
            "Уравнение реакции - 3;)"
        )
    )

    if action == 2:
        periodic_table_console()
        return

    if action == 3:
        chemistry_formula_selection(
            "Выберите вариант вычисления (обычно 1 для прямого расчёта): ",
            REACTION_STOICHIOMETRY,
        )
        return

    if action != 1:
        print("Неизвестное действие")
        return

    formula_number = int(
        input(
            "Выберите формулу общей химии:\n"
            + "\n".join(
                f"{number}. {title}" for number, title in GENERAL_CHEMISTRY.items()
            )
            + "\nНомер формулы: "
        )
    )

    selected_formula = GENERAL_CHEMISTRY.get(formula_number)
    if selected_formula is None:
        print("Неизвестная формула")
        return

    chemistry_formula_selection(
        "Выберите вариант вычисления (обычно 1 для прямого расчёта): ",
        formula_number,
    )


choice = int(
    input(
        "Выберите режим работы "
        "(Графический интерфейс - 1 ;"
        " Консольный режим - 2 ;)"
    )
)

match choice:
    case 1:
        from gui.app import UPCApp

        if __name__ == "__main__":
            UPCApp().run()
        else:
            sys.exit()
    case 2:
        category = int(
            input(
                "Выберите категорию "
                "(Физика - 1 ;"
                " Математика - 2 ;"
                " Свои формулы - 3 ;"
                " Химия - 4 ;)"
            )
        )

        match category:
            case 1:
                run_console_physics()
            case 2:
                run_console_math()
            case 3:
                run_console_custom()
            case 4:
                run_console_chemistry()
            case _:
                print("Неизвестная категория")