from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition

from gui.screens.MainScreen import MainScreen
from gui.screens.SectionScreen import SectionScreen
from gui.screens.TopicScreen import TopicScreen
from gui.screens.FormulaScreen import FormulaScreen


class UPCApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(SectionScreen(name="section_screen"))
        sm.add_widget(TopicScreen(name="topic_screen"))
        sm.add_widget(FormulaScreen(name="formula_screen"))
        sm.current = "main"
       
        return sm   