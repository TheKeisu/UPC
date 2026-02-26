from core.common.sections import section_selection
from core.common.sections import sections
import sys


def _read_float(prompt: str) -> float:
    value = input(prompt).strip().replace(",", ".")
    return float(value)


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
    import core.math.algebra.enum as algebra_enum
    import core.math.algebra.solver as algebra_solver

    branch = int(
        input(
            "Выберите раздел математики "
            "(Алгебра - 1;)"
        )
    )

    if branch != 1:
        print("Раздел математики пока недоступен")
        return

    formula = int(
        input(
            "Выберите формулу алгебры "
            "((a + b)^2 - 1;"
            " (a - b)^2 - 2;"
            " (a + b)(a - b) - 3;"
            " (a + b)^3 - 4;"
            " (a - b)^3 - 5;"
            " a^3 + b^3 - 6;"
            " a^3 - b^3 - 7;)"
        )
    )

    if formula not in algebra_enum.algebra:
        print("Неизвестная формула")
        return

    algebra_solver.formula_selection(algebra_enum.algebra[formula], formula)


def run_console_custom() -> None:
    from core.custom.formula_store import (
        add_custom_formula,
        list_custom_formulas,
        export_custom_formulas,
        import_custom_formulas,
    )
    from core.custom.solver import eval_expression, solve_equation, get_formula_symbols

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
        units_by_name = {
            item.get("name", "").strip().lower(): item.get("unit_symbol", "").strip()
            for item in variables
            if item.get("name")
        }
        variable_names = get_formula_symbols(formula_text)

        if not formula_text:
            print("У выбранной формулы нет выражения")
            return

        if "=" in formula_text:
            print(f"Доступные величины: {', '.join(variable_names)}")
            target = input("Что найти (обозначение): ").strip()
            if target.lower() not in {name.lower() for name in variable_names}:
                print("Неизвестная величина")
                return

            known_values: dict[str, float] = {}
            for variable_name in variable_names:
                if variable_name.lower() == target.lower():
                    continue
                unit = units_by_name.get(variable_name.lower())
                suffix = f" ({unit})" if unit else ""
                known_values[variable_name] = _read_float(f"Введите {variable_name}{suffix}: ")

            try:
                solutions = solve_equation(formula_text, target, known_values)
            except (TypeError, ValueError) as error:
                print(f"Ошибка вычисления: {error}")
                return

            if not solutions:
                print("Не удалось получить численное решение")
                return

            if len(solutions) == 1:
                print(f"{target} = {solutions[0]}")
            else:
                print(f"Возможные значения {target}: {', '.join(str(item) for item in solutions)}")
            return

        known_values: dict[str, float] = {}
        for variable_name in variable_names:
            unit = units_by_name.get(variable_name.lower())
            suffix = f" ({unit})" if unit else ""
            known_values[variable_name] = _read_float(f"Введите {variable_name}{suffix}: ")

        try:
            result = eval_expression(formula_text, known_values)
        except (TypeError, ValueError) as error:
            print(f"Ошибка вычисления: {error}")
            return

        print(f"Результат: {result}")
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
        name = input(f"Шаг 2. Величина {index}: ").strip()
        unit = input(f"Шаг 2. Обозначение единицы для величины {index}: ").strip()
        if not name or not unit:
            print("Величина и обозначение единицы обязательны")
            return
        variables.append({"name": name, "unit_symbol": unit})

    formula = input("Шаг 3. Введите формулу: ").strip()
    if not formula:
        print("Формула не может быть пустой")
        return

    add_custom_formula(title=title, variables=variables, formula=formula)
    print("Формула сохранена")


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
                " Свои формулы - 3 ;)"
            )
        )

        match category:
            case 1:
                run_console_physics()
            case 2:
                run_console_math()
            case 3:
                run_console_custom()
            case _:
                print("Неизвестная категория")