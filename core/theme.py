from kivy.properties import ListProperty
from kivy.event import EventDispatcher

class Theme(EventDispatcher):
    physics = ListProperty([0, 0.4, 0.8, 1])
    math = ListProperty([1, 0.4, 0, 1])
    chemistry = ListProperty([0, 0.6, 1, 1])
    custom = ListProperty([1, 0, 0, 1])

    default = ListProperty([1, 1, 1, 1])

theme = Theme()

SUBJECT_COLORS = {
    "физика": list(theme.physics),
    "свои формулы": list(theme.custom),
    "математика": list(theme.math),
    "химия": list(theme.chemistry),
}