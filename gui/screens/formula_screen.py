from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

from importlib import import_module

from core.calculation_registry import CALCULATION_MODULES
from core.formula_registry import ALL_DATA

Builder.load_file("gui/kv/formula_screen.kv")

class FormulaScreen(Screen):
    def load_formula(self, subject, section, formula_id):
        self.subject = subject
        self.section = section
        self.formula_id = formula_id

        # Получаем данные формулы
        data = ALL_DATA[subject][section][formula_id]
        data["subject_key"] = subject
        self.data = data

        self.ids.description_label.height = self.ids.formula_label.texture_size[1]
        self.ids.formula_label.height = self.ids.formula_label.texture_size[1]
        self.ids.description_label.opacity = 1
        self.ids.formula_label.opacity = 1
        self.ids.description_label.disabled = False
        self.ids.formula_label.disabled = False
        self.ids.title_label.text = data["title"]
        self.ids.description_label.text = data.get("description", "")
        self.ids.formula_label.text = data.get("formula_view", "")

        # Очищаем контейнеры
        self.ids.cases_container.clear_widgets()
        self.ids.inputs_container.clear_widgets()
        self.ids.inputs_container.opacity = 0
        self.ids.inputs_container.disabled = True
        self.ids.result_label.text = ""

        # Создаём кнопки выбора кейсов
        for case_id, case in data["cases"].items():
            btn = Button(
                text=case["name"],
                size_hint_y=None,
                height=50
            )
            btn.bind(on_press=lambda x, cid=case_id: self.build_inputs(cid))
            self.ids.cases_container.add_widget(btn)

    def build_inputs(self, case_id):
        case = self.data["cases"][case_id]

        # Скрываем список кейсов
        self.ids.cases_container.clear_widgets()
        

        self.ids.inputs_container.clear_widgets()
        self.inputs = {}

        # Делаем контейнер видимым и скрываем заголовки
        self.ids.formula_label.height = self.ids.formula_label.texture_size[1]
        self.ids.description_label.height = 0
        self.ids.formula_label.height = 0
        self.ids.description_label.opacity = 0
        self.ids.formula_label.opacity = 0
        self.ids.description_label.disabled = True
        self.ids.formula_label.disabled = True
        self.ids.inputs_container.opacity = 1
        self.ids.inputs_container.disabled = False
        self.ids.result_label.text = ""

        # Добавляем поля ввода
        for key, label_text in case["inputs"]:
            self.ids.inputs_container.add_widget(Label(
                text=label_text,
                size_hint_y=None,
                height=30
            ))
            input_field = TextInput(multiline=False, size_hint_y=None, height=40)
            self.inputs[key] = input_field
            self.ids.inputs_container.add_widget(input_field)

        # Кнопка расчёта
        calc_btn = Button(
            text="Рассчитать",
            size_hint_y=None,
            height=50
        )
        calc_btn.bind(on_press=lambda x: self.calculate(self.subject, self.data, case))
        self.ids.inputs_container.add_widget(calc_btn)

    def calculate(self, subject, data, case):
        try:
            values = []
            for key, widget in self.inputs.items():
                text_value = widget.text
                if not text_value:
                    self.ids.result_label.text = "Пожалуйста, заполните все поля"
                    return
                values.append(float(text_value))

            # Определяем модуль вычислений
            module = CALCULATION_MODULES[subject]

            # Получаем функцию
            func = self.get_function_from_path(case["function"])

            # Вызываем функцию
            result = func(*values)

            # Выводим результат
            self.ids.result_label.text = f"{case['output']} = {result} {case.get('SI', '')}"

        except ValueError:
            self.ids.result_label.text = "Введите корректные числа"
        except Exception as e:
            self.ids.result_label.text = f"Ошибка вычислений: {str(e)}"

    def get_function_from_path(self, path: str):
        module_path, func_name = path.rsplit('.', 1)
        module = import_module(module_path)
        return getattr(module, func_name)

    def go_back(self):
        self.manager.current = "topic_screen"