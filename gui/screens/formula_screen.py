KEYWORDS_TO_CATEGORIES = {
    "заряд": "charge",
    "расстояние": "length",
    "длина": "length",
    "радиус": "length",
    "путь": "length",
    "масса": "mass",
    "время": "time",
    "период": "time",
    "температура": "temperature",
    "ток": "current",
    "напряжение": "voltage",
    "сопротивление": "resistance",
    "мощность": "power",
    "энергия": "energy",
    "давление": "pressure",
    "сила": "force",
    "силу": "force",
    "частота": "frequency",
    "емкость": "capacitance",
    "площадь": "area",
    "объем": "volume",
    "плотность": "density",
    "высота": "length",
    "скорость": "velocity",
    "угловая скорость": "angular_velocity",
    "начальная скорость": "velocity",
    "ускорение": "acceleration",
    "стремительность": "acceleration",
    "жесткость пружины": "stiffness",
    "угол": "angle",
    "деформация": "length",
    "импульс": "momentum",
    "импульс тела": "momentum",
    "импульс силы": "momentum",
    "коэффициент": "coefficient",
    "коэффициент трения": "coefficient",
    "момент силы": "moment_torque",
    "плечо силы": "length",
    "работа": "work",
    "КПД": "efficiency",
    "Затраченная работа": "energy",
    "Полезная работа": "energy",
    "амплитуда": "length",
    "напряженность электрического поля": "electric_field_strength",
    "напряженность электрического поля в вакууме": "electric_field_strength",
    "напряженность электрического поля в диэлектрике": "electric_field_strength",
    "потенциал": "potential_difference",
    "электрический потенциал": "potential_difference",
    "потенциальная энергия": "energy",
    "количество теплоты": "energy",
    "вектор магнитной индукции": "magnetic_field_strength",
    "длина проводника": "length",
    "сила тока": "current",
    "напряжение на проводнике": "voltage",
    "магнитная индукция": "magnetic_field_strength",
    "энергия магнитного поля": "energy",
    "энергия магнитного поля катушки": "energy",
    "энергия электрического поля": "energy",
    "индуктивность": "inductance",
    "угловая частота": "angular_velocity",
    "напряжение": "voltage",
    "амплитуда напряжения": "voltage",
    "изображение": "length",
    "шаг решетки": "length",
    "молярная масса": "molar_mass",
    "изменение объема": "volume",
    "изменение температуры": "temperature",
    "теплота": "energy",
    "изменение внутренней энергии": "energy",
    
    
}
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from importlib import import_module

from core.calculation_registry import CALCULATION_MODULES
from core.formula_registry import ALL_DATA

from gui.round_button import RoundButton

import json
try:
    with open("core/convertorSI/SIunits.json", "r", encoding="utf-8") as f:
        UNITS_CONFIG = json.load(f)
except Exception as e:
    print(f"Не удалось загрузить SIunits.json: {e}")
    UNITS_CONFIG = {}
    
Builder.load_file("gui/kv/formula_screen.kv")
Builder.load_file("gui/kv/round_button.kv")
Builder.load_file("gui/kv/back_button.kv")

class FormulaScreen(Screen):
    def on_pre_enter(self):
        """Срабатывает ПЕРЕД тем, как экран отобразится пользователю"""
        self.reset_ui_state()
    
    def load_formula(self, subject, section, formula_id):
        self.reset_ui_state()
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
        self.ids.inputs_section.clear_widgets()
        self.ids.inputs_section.opacity = 0
        self.ids.inputs_section.disabled = True
        self.ids.inputs_section.clear_widgets()
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

        self.ids.theory_section.opacity = 0
        self.ids.theory_section.height = 0
        self.ids.theory_section.disabled = True

        self.ids.inputs_section.clear_widgets()
        self.ids.inputs_section.opacity = 1
        self.ids.inputs_section.disabled = False
        self.inputs = {}
        

        # Добавляем поля ввода
        for key, label_text in case["inputs"]:
    # Метка (название поля)
            self.ids.inputs_section.add_widget(Label(
            text=label_text,
            size_hint_y=None,
            height=50,
            text_size= (self.width * 0.8, None),
            halign="center",
            color=(0, 0.4, 0.8, 1),
            font_size="22sp",
            bold=True
    ))
    
    # Текстовое поле - КРИТИЧНО: добавляем обертку или ограничиваем ширину
            input_field = FormulaTextInput(label_text=label_text)
            self.inputs[key] = input_field
            self.ids.inputs_section.add_widget(input_field)

        # Кнопка расчета должна быть такой же ширины
        calc_btn = RoundButton(
            text="Рассчитать",
            size_hint=(1, None),
            height=80,
            subject=self.subject
        )
        calc_btn.bind(on_press=lambda x: self.calculate(self.subject, self.data, case))
        
        # Добавляем небольшой отступ перед кнопкой
        self.ids.inputs_section.add_widget(Label(size_hint_y=None, height=20))
        self.ids.inputs_section.add_widget(calc_btn)
        
        self.ids.cases_container.opacity = 0
        self.ids.cases_container.disabled = True

    def calculate(self, subject, data, case):
        try:
            values = []
            for key, widget in self.inputs.items():
                si_val = widget.get_value_in_si()
                if si_val is None:
                    self.show_result("Заполните все поля!")
                    return
                values.append(si_val)
        
                widget.text = ""

            func = self.get_function_from_path(case["function"])
            result = func(*values)

            # Округляем результат до 4 знаков для красоты
            formatted_res = round(result, 4)
            self.show_result(f"{case['output']} = {formatted_res} {case.get('SI', '')}")

        except ValueError:
            self.show_result("Введите числа!")
        except Exception as e:
            self.show_result(f"Ошибка: {str(e)}")

    def show_result(self, text):
        """Вспомогательный метод для отображения блока результата"""
        self.ids.result_label.text = text
        self.ids.result_box.opacity = 1
        self.ids.result_box.disabled = False
        # Устанавливаем высоту, чтобы BoxLayout пересчитал макет
        self.ids.result_box.height = 100

    def get_function_from_path(self, path: str):
        module_path, func_name = path.rsplit('.', 1)
        module = import_module(module_path)
        return getattr(module, func_name)

    def go_back(self):
        # Если мы сейчас в режиме ввода данных (секция инпутов видна)
        if self.ids.inputs_section.opacity == 1:
            # Возвращаем всё назад к выбору кейсов внутри этого же экрана
            self.reset_ui_state()
        else:
            # Если мы и так на главном виде формулы, выходим на предыдущий экран
            self.manager.current = "topic_screen"

    def reset_ui_state(self):
        """Возвращает экран в исходное состояние (Теория + Кнопки кейсов)"""
        # 1. Показываем теорию, скрываем инпуты в синем боксе
        self.ids.theory_section.opacity = 1
        self.ids.theory_section.height = self.ids.theory_section.minimum_height
        self.ids.theory_section.disabled = False
        
        self.ids.inputs_section.opacity = 0
        self.ids.inputs_section.height = 0
        self.ids.inputs_section.disabled = True
        self.ids.inputs_section.clear_widgets() # Очищаем старые поля

        # 2. Показываем кнопки выбора кейсов (GridLayout в ScrollView)
        self.ids.cases_container.opacity = 1
        self.ids.cases_container.height = self.ids.cases_container.minimum_height
        self.ids.cases_container.disabled = False
        
        # 3. Скрываем блок результата
        self.ids.result_box.opacity = 0
        self.ids.result_box.height = 0
        self.ids.result_label.text = ""
    
class FormulaTextInput(BoxLayout):
    def __init__(self, label_text="", **kwargs):
        super().__init__(**kwargs)
        self.category = None
        
        # Автоматически определяем категорию физической величины по тексту
        label_text_lower = label_text.lower()
        for keyword, category_name in KEYWORDS_TO_CATEGORIES.items():
            if keyword in label_text_lower:
                self.category = category_name
                break
                
        self.setup_spinner()

    def setup_spinner(self):
        """Заполняет выпадающий список единицами измерения"""
        if self.category and self.category in UNITS_CONFIG:
            units_dict = UNITS_CONFIG[self.category]["units"]
            self.ids.unit_spinner.values = list(units_dict.keys())
            self.ids.unit_spinner.text = UNITS_CONFIG[self.category]["base"]
        else:
            # Если это безразмерный коэффициент, скрываем выпадающий список
            self.ids.unit_spinner.values = ['-']
            self.ids.unit_spinner.text = '-'
            self.ids.unit_spinner.disabled = True
            self.ids.unit_spinner.opacity = 0

    @property
    def text(self):
        return self.ids.text_input.text
    
    @text.setter
    def text(self, value):
        self.ids.text_input.text = value

    def get_value_in_si(self):
        """Переводит введенное число в СИ перед расчетом"""
        raw_text = self.text.replace(',', '.')
        if not raw_text:
            return None
        
        value = float(raw_text)
        
        # Если категория не определилась, возвращаем число как есть
        if not self.category or self.category not in UNITS_CONFIG:
            return value
            
        current_unit = self.ids.unit_spinner.text
        
        # Особый случай для температуры (Цельсии)
        if current_unit == "°C":
            return value + 273.15
            
        # Для всех остальных величин просто умножаем на коэффициент из JSON
        multiplier = UNITS_CONFIG[self.category]["units"][current_unit]
        return value * multiplier