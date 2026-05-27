from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.core.window import Window

from kivy.lang import Builder

from core.theme import SUBJECT_COLORS
from gui.round_button import RoundButton


Builder.load_file("gui/kv/section_screen.kv")
Builder.load_file("gui/kv/back_button.kv")
Builder.load_file("gui/kv/round_button.kv")

subjects = ["математика", "физика", "химия", "свои формулы"]


class SectionScreen(Screen):

    def on_enter(self):
        Clock.schedule_once(self.load_buttons, 0)
    
    def load_buttons(self, dt=0):
        self.ids.sections_box.clear_widgets()
        
        current_subjects = getattr(self, "section", None)
        if not self.section:
            return  # если по какой-то причине нет предмета, выходим
    
        sections = self.get_sections(self.section)
        
        sub_sections = self.get_sections(current_subjects)
        
        for item in sub_sections:    
            btn = RoundButton(
                text=item.capitalize(),
                subject=current_subjects,
                width= Window.width * 0.439,    
                height= Window.height * 0.12)
            btn.bind(on_press=lambda x, s=item: self.open_section(s))
            self.ids.sections_box.add_widget(btn)


    def get_sections(self, section):

        if section == "физика":
            return ["механика", "электродинамика", "оптика", "термодинамика"]

        if section == "свои формулы":
            return ["кастомные формулы"]

        return []

    def open_section(self, section_name):
        topic_screen = self.manager.get_screen("topic_screen")
        topic_screen.load_buttons(self.section, section_name)
        self.manager.current = "topic_screen"
        
    def go_back(self):
        self.manager.current = "main_screen"
        

        
class BackButton(Button):
    pass

