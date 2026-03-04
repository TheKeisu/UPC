from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


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
            size_hint_y=None,
            padding=20
        ))
        
        formulas = self.get_formulas(subject, section)
        self.formulas = formulas
        
        self.search_input = TextInput(
                size_hint_y=None,
                height=40,
                hint_text="Поиск формулы...",
                multiline=False
            )
        self.search_input.bind(text = self.filter_formulas)
        bl.add_widget(self.search_input)
        
        self.gl = gl

        for key, data in formulas.items():
            btn = Button(
                text=data["title"],
                size_hint_y=None,
                height=40
                         )
            btn.bind(on_press=lambda x, k=key: self.open_formula(k))
            gl.add_widget(btn)

#Create ScrollView
        scroll_view = ScrollView(size_hint=(1, .8))
        scroll_view.add_widget(gl)
        
 #BACK BUTTON
        back_button = Button(
            text="<- Назад",
            size_hint_y=None,
            height=50,
            on_press=lambda x: setattr(self.manager, "current", "section_screen")
        )
        
        bl.add_widget(scroll_view)
        bl.add_widget(back_button)
        self.add_widget(bl)
        
    def filter_formulas(self,instance, value):
        self.gl.clear_widgets()
        
        query = value.lower()
        
        for key, data in self.formulas.items():
            if query in data["title"].lower():
                btn = Button(
                    text=data["title"],
                    size_hint_y=None,
                    height=40
                )
                btn.bind(on_press=lambda x, k=key: self.open_formula(k))
                self.gl.add_widget(btn)

    def get_formulas(self, subject, section):
        from core.formula_registry import ALL_DATA
        return ALL_DATA[subject][section]

    def open_formula(self, formula_id):
        formula_screen = self.manager.get_screen("formula_screen")
        formula_screen.load_formula(self.subject, self.section, formula_id)
        self.manager.current = "formula_screen"