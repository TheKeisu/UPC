from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.clock import Clock


Builder.load_file("gui/kv/section_screen.kv")
Builder.load_file("gui/kv/back_button.kv")

subjects = ["математика", "физика", "химия", "свои формулы"]


class SectionScreen(Screen):

    def on_enter(self):
        Clock.schedule_once(self.load_buttons, 0)
    
    def load_buttons(self, dt=0):
        self.ids.sections_box.clear_widgets()
    
        if not self.section:
            return  # если по какой-то причине нет предмета, выходим
    
        sections = self.get_sections(self.section)
    
        for section in sections:
            btn_color = (1, 1, 1, 1)  # белый по умолчанию
            if section == "свои формулы":
                btn_color = (1, 0, 0, 1)
            elif section == "математика":
                btn_color = (1, 0.4, 0, 1)
            elif section == "физика":
                btn_color = (0, 0.4, 0.8, 1)
            elif section == "химия":
                btn_color = (0, 0.6, 1, 1)
            
            btn = RoundButton(text=section.capitalize())
            btn.bg_color = btn_color
            btn.bind(on_press=lambda x, s=section: self.open_section(s))
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

class RoundButton(Button):
    bg_color = (ListProperty([1, 1, 1, 1])) # Белый цвет
    
    pass