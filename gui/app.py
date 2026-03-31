from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition
from kivy.core.window import WindowBase

from gui.screens.main_screen import MainScreen
from gui.screens.section_screen import SectionScreen
from gui.screens.topic_screen import TopicScreen
from gui.screens.formula_screen import FormulaScreen


class UPCApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainScreen(name="main_screen"))
        sm.add_widget(SectionScreen(name="section_screen"))
        sm.add_widget(TopicScreen(name="topic_screen"))
        sm.add_widget(FormulaScreen(name="formula_screen"))
        sm.current = "main_screen"
       
        return sm   