from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from importlib import import_module

from core.calculation_registry import CALCULATION_MODULES
from core.formula_registry import ALL_DATA

class FormulaScreen(Screen):   
    def load_formula(self, subject, section, formula_id, case_id=1):
        self.clear_widgets()
        
        # Получаем данные формулы
        data = ALL_DATA[subject][section][formula_id]
        data["subject_key"] = subject
        
        # Главный layout
        bl = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=40
        )

        # Заголовок
        bl.add_widget(Label(
            text=data["title"],
            font_size=28,
            size_hint = (1, 0.2))
        )
        
        # Описание
        bl.add_widget(Label(
            text=data.get("description", ""),
            size_hint = (1, 0.1)
            ))
        # Формула
        bl.add_widget(Label(
            text=data["formula_view"],
            size_hint = (1, 0.1)
            ))
        
        # Варианты
        for case_id, case in data["cases"].items():
            btn = Button(
                text=case["name"],
               on_press=lambda x, subj=subject, f=data, cid=case_id: self.build_inputs(subj, f, cid)
            )
            bl.add_widget(btn)
        #Кнопка назад
        back_button = Button(
            text="<- Назад",
            on_press=lambda x: setattr(self.manager, "current", "topic_screen")
        )

        bl.add_widget(back_button)
        self.add_widget(bl)
    def build_inputs(self, subject, data, case_id):
        self.clear_widgets()
        
        case = data["cases"][case_id]
        
        bl = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=40
        )
        
        self.inputs = {}
        
        for key, label_text in case["inputs"]:
            bl.add_widget(Label(text=label_text))
            input_field = TextInput(multiline=False)
            self.inputs[key] = input_field
            bl.add_widget(input_field)
        
        bl.add_widget(Button(
            text="Рассчитать",
            on_press=lambda x, subj = subject, c=case: self.calculate(subj,data, c)
        ))
        
        self.result_label = Label(text="")
        bl.add_widget(self.result_label)
        
        back_button = Button(
            text="<- Назад",
            on_press=lambda x: setattr(self.manager, "current", "topic_screen")
        )

        bl.add_widget(back_button)

        self.add_widget(bl)      
    def calculate(self, subject, data, case):
        try:
            # Забираем значения из полей ввода
            values = []
            for key, widget in self.inputs.items():
                text_value = widget.text
                if not text_value:
                    self.result_label.text = "Пожалуйста, заполните все поля"
                    return
                
                values.append(float(text_value))
                
            #Определяем модуль вычислений
            subject_key = data["subject_key"]
            module = CALCULATION_MODULES[subject]
            
            #Получаем функцию для расчета
            func_path = case["function"]
            func = self.get_function_from_path(func_path)
            
            #Вызываем функцию
            result = func(*values)
            
            #Выводим результат
            self.result_label.text = f"{case['output']} = {result} {case.get('SI', '')}"
        
        except ValueError:
            self.result_label.text = "Введите корректные числа"
            
        except Exception as e:
            self.result_label.text = "Ошибка вычислений"
    
    def get_function_from_path(self, path: str):
        module_path, func_name = path.rsplit('.', 1)
        module = import_module(module_path)
        return getattr(module, func_name)