from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class FormulaScreen(Screen):

    def load_formula(self, subject, section, formula_id):
        from core.formula_registry import ALL_DATA

        data = ALL_DATA[subject][section][formula_id]

        self.clear_widgets()

        layout = BoxLayout(orientation="vertical", spacing=20, padding=40)

        layout.add_widget(Label(text=data["title"], font_size=28))
        layout.add_widget(Label(text=data["formula_view"]))
        layout.add_widget(Label(text=data.get("description", "")))

        layout.add_widget(Button(
            text="<- Назад",
            on_press=lambda x: setattr(self.manager, "current", "topic_screen")
        ))

        self.add_widget(layout)