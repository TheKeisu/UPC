from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.properties import StringProperty

SUBJECT_COLORS = {
    "физика": [0, 0.4, 0.8, 1],
    "свои формулы": [1, 0, 0, 1],
    "математика": [1, 0.4, 0, 1],
    "химия": [0, 0.6, 1, 1]
}

class RoundButton(ButtonBehavior, Label):
    bg_color = ListProperty([1, 1, 1, 1])
    subject = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_subject(self, self.subject)

    
    def on_subject(self, instance, value):
        color = SUBJECT_COLORS.get(value, (1, 1, 1, 1))  # белый по умолчанию
        self.bg_color = SUBJECT_COLORS.get(value, [1, 1, 1, 1])
    
class SmallRoundButton(ButtonBehavior, Label):
    bg_color = ListProperty([1, 1, 1, 1]) # Белый цвет
    subject = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_subject(self, self.subject)

    
    def on_subject(self, instance, value):
        color = SUBJECT_COLORS.get(value, (1, 1, 1, 1))
        self.bg_color = SUBJECT_COLORS.get(value, [1, 1, 1, 1])