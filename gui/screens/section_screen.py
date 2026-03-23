from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("gui/kv/section_screen.kv")

class SectionScreen(Screen):

    def load_subject(self, subject_name):
        self.subject = subject_name

        sections = self.get_sections(subject_name)

        # очищаем кнопки
        self.ids.sections_box.clear_widgets()

        for section in sections:
            btn = Button(
                text=section.capitalize(),
                size_hint_y=None,
                height=60
            )

            btn.bind(on_press=lambda x, s=section: self.open_section(s))
            self.ids.sections_box.add_widget(btn)

    def get_sections(self, subject):

        if subject == "физика":
            return ["механика", "электродинамика", "оптика", "термодинамика"]

        if subject == "свои формулы":
            return ["кастомные формулы"]

        return []

    def open_section(self, section_name):
        topic_screen = self.manager.get_screen("topic_screen")
        topic_screen.load_section(self.subject, section_name)
        self.manager.current = "topic_screen"