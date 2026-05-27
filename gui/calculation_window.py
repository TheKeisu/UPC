from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

class CalculatorWidget(BoxLayout):
    formula = StringProperty("0")

    def append_symbol(self, symbol):
        if self.formula == "0" or self.formula == "Error":
            self.formula = symbol
        else:
            self.formula += symbol

    def clear_screen(self):
        self.formula = "0"

    def calculate(self):
        try:
            # Безопасно вычисляем простую строку math-выражения
            self.formula = str(eval(self.formula))
        except Exception:
            self.formula = "Error"