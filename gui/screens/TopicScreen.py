from cProfile import label
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class TopicScreen(Screen):

    def load_section(self, subject, section):
        self.subject = subject
        self.section = section

        self.clear_widgets()

        bl = BoxLayout(orientation="vertical", spacing=20, padding=40)
        gl = GridLayout(cols=1, spacing = 10, size_hint_y=None, padding=40)
        gl.bind(minimum_height=gl.setter('height'))

        bl.add_widget(Label(
            text=f"Выберите формулу из раздела {section.capitalize()}",
            font_size=28,
            size_hint=(1, .2),
        ))

        formulas = self.get_formulas(subject, section)

        for key, data in formulas.items():
            btn = Button(text=data["title"], size_hint_y=None, height=40)
            btn.bind(on_press=lambda x, k=key: self.open_formula(k))
            gl.add_widget(btn)

#Create ScrollView
        scroll_view = ScrollView(size_hint=(1, .8))
        scroll_view.add_widget(gl)
        
 #BACK BUTTON
        back_button = Button(
            text="<- Назад",
            size_hint=(1, .2),
            on_press=lambda x: setattr(self.manager, "current", "section_screen")
        )
        
        bl.add_widget(scroll_view)
        bl.add_widget(back_button)
        self.add_widget(bl)

    def get_formulas(self, subject, section):
        from core.formula_registry import ALL_DATA
        return ALL_DATA[subject][section]

    def open_formula(self, formula_id):
        formula_screen = self.manager.get_screen("formula_screen")
        formula_screen.load_formula(self.subject, self.section, formula_id)
        self.manager.current = "formula_screen"