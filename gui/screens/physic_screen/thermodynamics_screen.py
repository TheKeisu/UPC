from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ThermodynamicsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        bl_tds = BoxLayout(orientation="vertical", spacing=20, padding=40)
        
        bl_tds.add_widget(Button(
            text="<- Назад",
            size_hint=(1, .5),
            on_press=lambda x: setattr(self.manager, "current", "physics_screen")
        ))
        self.add_widget(bl_tds)