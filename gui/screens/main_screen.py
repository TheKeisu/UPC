from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("gui/kv/main_screen.kv")

class MainScreen(Screen):
    
    def on_enter(self):
        subjects = ["математика", "физика", "химия", "свои формулы"]
        
        self.ids.subjects_box.clear_widgets()
        
        for subject in subjects:
            btn = Button(text=subject.capitalize())
            btn.bind(on_press=lambda x, s=subject: self.open_subject(s))
            self.ids.subjects_box.add_widget(btn)
            
    def open_subject(self, subject_name):  
        # if subject_name == "свои формулы":
        #     self.manager.current = "custom_formula_screen"
        # else:
            section_screen = self.manager.get_screen("section_screen")
            section_screen.load_subject(subject_name)
            self.manager.current = "section_screen"