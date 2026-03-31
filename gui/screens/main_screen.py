from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.clock import Clock

Builder.load_file("gui/kv/main_screen.kv")

Window.clearcolor = (1, 1, 1, 1)
Window.size = (1920, 1080)
Window.fullscreen = True
subjects = ["математика", "физика", "химия", "свои формулы"]

class RoundButton(Button):
    bg_color = ListProperty([1, 1, 1, 1]) # Белый цвет
    pass
class MainScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.load_buttons, 0)
    
    def load_buttons(self, dt):
        self.ids.subjects_box.clear_widgets()
        
        for subject in subjects:
            if subject == "свои формулы":
                btn_color=(1, 0, 0, 1)  # Красный цвет для своих формул
            elif subject == "математика":
                btn_color=(1, 0.4, 0, 1)  # Оранжевый цвет для математики
            elif subject == "физика":
                btn_color=(0, 0.4, 0.8, 1)  # Синий цвет для физики
            elif subject == "химия":
                btn_color=(0, 0.6, 1, 1)  # Голубой цвет для химии
            btn = RoundButton(text=subject.capitalize())
            btn.bg_color = btn_color
            btn.bind(on_press=lambda x, s=subject: self.open_subject(s))
            self.ids.subjects_box.add_widget(btn)
            
        
            
    def open_subject(self, subject_name):  
        # if subject_name == "свои формулы":
        #     self.manager.current = "custom_formula_screen"
        # else:
            section_screen = self.manager.get_screen("section_screen")
            section_screen.section = subject_name
            section_screen.load_buttons(subject_name)
            self.manager.current = "section_screen"
            