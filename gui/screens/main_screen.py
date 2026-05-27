from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.clock import Clock

from gui.round_button import RoundButton

Builder.load_file("gui/kv/main_screen.kv")
Builder.load_file("gui/kv/round_button.kv")

Window.clearcolor = (1, 1, 1, 1)
Window.size = (1920, 1080)
Window.fullscreen = False

subjects = ["математика", "физика", "химия", "свои формулы"]


class MainScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.load_buttons, 0)
    
    def load_buttons(self, dt):
        self.ids.subjects_box.clear_widgets()
        
        for subject in subjects:
            btn = RoundButton(
                text=subject.capitalize(),
                subject=subject,
                width= Window.width * 0.439,    
                height= Window.height * 0.12
            )
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
            