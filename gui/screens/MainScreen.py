from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=20, padding=40)

        layout.add_widget(Label(
            text="Выберите предмет",
            font_size=32,
            size_hint=(1, .2),
        ))

        subjects = ["математика", "физика", "химия", "свои формулы"]

        for subject in subjects:
            btn = Button(text=subject.capitalize())
            btn.bind(on_press=lambda x, s=subject: self.open_subject(s))
            layout.add_widget(btn)

        self.add_widget(layout)

    def open_subject(self, subject_name):
        # if subject_name == "свои формулы":
        #     self.manager.current = "custom_formula_screen"
        #     return

        section_screen = self.manager.get_screen("section_screen")
        section_screen.load_subject(subject_name)
        self.manager.current = "section_screen"