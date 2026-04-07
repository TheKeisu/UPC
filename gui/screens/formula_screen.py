from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.properties import ListProperty

from importlib import import_module

from core.calculation_registry import CALCULATION_MODULES
from core.formula_registry import ALL_DATA

from gui.round_button import RoundButton

Builder.load_file("gui/kv/formula_screen.kv")
Builder.load_file("gui/kv/round_button.kv")
Builder.load_file("gui/kv/back_button.kv")

class FormulaScreen(Screen):
    def load_formula(self, subject, section, formula_id):
        self.subject = subject
        self.section = section
        self.formula_id = formula_id
        
        data = ALL_DATA[subject][section][formula_id]
        self.data = data

        # Сброс видимости элементов (показываем описание и формулу)
        self.toggle_info_visibility(show=True)
        
        self.ids.title_label.text = data["title"]
        self.ids.description_label.text = data.get("description", "")
        self.ids.formula_label.text = data.get("formula_view", "")

        # Очистка контейнеров
        self.ids.cases_container.clear_widgets()
        self.ids.inputs_container.clear_widgets()
        self.ids.inputs_container.opacity = 0
        self.ids.inputs_container.disabled = True
        self.ids.inputs_container.clear_widgets()
        self.ids.result_box.opacity = 0
        self.ids.result_box.disabled = True
        self.ids.result_label.text = ""

        # Создаём кнопки выбора кейсов (центрированные)
        for case_id, case in data["cases"].items():
            btn = RoundButton(
            text=case["name"],
            size_hint=(0.85, None), # Растянется на ширину родительского BoxLayout (80% экрана)
            height=80,
            subject=subject
            )
            btn.bind(on_press=lambda x, cid=case_id: self.build_inputs(cid))
            self.ids.cases_container.add_widget(btn)

    def toggle_info_visibility(self, show=True):
        """Переключает видимость верхнего блока и подстраивает макет"""
        if show:
            self.ids.information_box.opacity = 1
            self.ids.information_box.size_hint_y = None # Позволяем расширяться по тексту
            self.ids.information_box.disabled = False
        else:
            self.ids.information_box.opacity = 0
            self.ids.information_box.size_hint_y = 0 # Убираем занимаемое место
            self.ids.information_box.disabled = True

    def build_inputs(self, case_id):
        case = self.data["cases"][case_id]

        # Очищаем список выбора, чтобы он не мешал полям ввода
        self.ids.cases_container.clear_widgets()
        self.ids.inputs_container.clear_widgets()
        self.inputs = {}

        # Скрываем верхний блок с теорией, чтобы освободить место
        self.toggle_info_visibility(show=False)

        # Показываем контейнер для ввода
        self.ids.inputs_container.opacity = 1
        self.ids.inputs_container.disabled = False
        self.ids.result_box.opacity = 1
        self.ids.result_box.disabled = False

        # Добавляем поля ввода
        for key, label_text in case["inputs"]:
    # Метка (название поля)
            self.ids.inputs_container.add_widget(Label(
            text=label_text,
            size_hint_y=None,
            height=25,
            color=(0,0,0,0.7),
            font_size="30sp"
    ))
    
    # Текстовое поле - КРИТИЧНО: добавляем обертку или ограничиваем ширину
            input_field = FormulaTextInput()
            self.inputs[key] = input_field
            self.ids.inputs_container.add_widget(input_field)

        # Кнопка расчета должна быть такой же ширины
        calc_btn = RoundButton(
            text="Рассчитать",
            size_hint=(1, None),
            height=60,
            subject=self.subject
        )
        calc_btn.bind(on_press=lambda x: self.calculate(self.subject, self.data, case))
        
        # Добавляем небольшой отступ перед кнопкой
        self.ids.inputs_container.add_widget(Label(size_hint_y=None, height=20))
        self.ids.inputs_container.add_widget(calc_btn)

    def calculate(self, subject, data, case):
        try:
            values = []
            for key, widget in self.inputs.items():
                val = widget.text.replace(',', '.') # Замена запятой на точку для удобства
                if not val:
                    self.ids.result_label.text = "Заполните все поля!"
                    return
                values.append(float(val))

            func = self.get_function_from_path(case["function"])
            result = func(*values)

            # Округляем результат до 4 знаков для красоты
            formatted_res = round(result, 4)
            self.ids.result_label.text = f"{case['output']} = {formatted_res} {case.get('SI', '')}"

        except ValueError:
            self.ids.result_label.text = "Введите числа!"
        except Exception as e:
            self.ids.result_label.text = f"Ошибка: {str(e)}"

    def get_function_from_path(self, path: str):
        module_path, func_name = path.rsplit('.', 1)
        module = import_module(module_path)
        return getattr(module, func_name)

    def go_back(self):
        # Если мы в режиме ввода данных, то первый "назад" вернет нас к выбору кейсов
        if self.ids.inputs_container.opacity == 1:
            self.load_formula(self.subject, self.section, self.formula_id)
        else:
            self.manager.current = "topic_screen"
    
class FormulaTextInput(TextInput):
    pass