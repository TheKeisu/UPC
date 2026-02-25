from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MechanicsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        bl_ms = BoxLayout(orientation="vertical", spacing=20, padding=40)
        
        bl_ms.add_widget(Button(
            text="<- Назад",
            size_hint=(1, .5),
            on_press=lambda x: setattr(self.manager, "current", "physics_screen")
        ))
        self.add_widget(bl_ms)