from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SectionScreen(Screen):

    def load_subject(self, subject_name):
        self.subject = subject_name

        self.clear_widgets()

        layout = BoxLayout(orientation="vertical", spacing=20, padding=40)

        layout.add_widget(Label(
            text="Выберите раздел",
            font_size=28,
            size_hint=(1, .2),
        ))

        sections = self.get_sections(subject_name)

        for section in sections:
            btn = Button(text=section.capitalize())
            btn.bind(on_press=lambda x, s=section: self.open_section(s))
            layout.add_widget(btn)

        layout.add_widget(Button(
            text="<- Назад",
            on_press=lambda x: setattr(self.manager, "current", "main")
        ))

        self.add_widget(layout)

    def get_sections(self, subject):
        # пример
        if subject == "физика":
            return ["механика", "электродинамика", "оптика", "термодинамика"]
        return []

    def open_section(self, section_name):
        topic_screen = self.manager.get_screen("topic_screen")
        topic_screen.load_section(self.subject, section_name)
        self.manager.current = "topic_screen"