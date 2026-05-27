from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.core.window import Window

from gui.round_button import SmallRoundButton

Builder.load_file("gui/kv/topic_screen.kv")
Builder.load_file("gui/kv/small_round_button.kv")


class TopicScreen(Screen):

    def load_buttons(self, subject, section):
        self.subject = subject
        self.section = section

        self.ids.title_label.text = f"Выберите формулу из раздела {section.capitalize()}"

        self.formulas = self.get_formulas(subject, section)

        self.update_buttons(self.formulas)

    def update_buttons(self, formulas):
        grid = self.ids.formulas_grid
        grid.clear_widgets()

        for key, data in formulas.items():
            btn = SmallRoundButton(
                text=data.get("title", "Без названия"),
                size_hint_y=None,
                height=60,
                width= Window.width * 0.439, 
                font_size=20,
                subject=self.subject 
            )
            btn.bind(on_press=lambda x, k=key: self.open_formula(k))
            grid.add_widget(btn)

    def filter_formulas(self, value):
        query = value.lower()

        filtered = {
            k: v for k, v in self.formulas.items()
            if query in v.get("title", "").lower()
            or query in v.get("formula", "").lower()
        }

        self.update_buttons(filtered)

    def get_formulas(self, subject, section):
        from core.formula_registry import ALL_DATA
        return ALL_DATA[subject][section]

    def open_formula(self, formula_id):
        formula_screen = self.manager.get_screen("formula_screen")
        formula_screen.load_formula(self.subject, self.section, formula_id)
        self.manager.current = "formula_screen"

    def go_back(self):
        self.manager.current = "section_screen"
