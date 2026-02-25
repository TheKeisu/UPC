from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class PhysicsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
        bl_ps = BoxLayout(orientation="vertical", spacing=20, padding=40)
        

        bl_ps.add_widget(Label(
            text="Выберите раздел",
            font_size=32,
            size_hint=(1, .2),
        ))
        
        bl_ps.add_widget(Button(
            text="Mechanics",
            on_press=lambda x: self.go_to("mechanics_screen")
        ))

        bl_ps.add_widget(Button(
            text="Electrodynamics",
            on_press=lambda x: self.go_to("electrodynamics_screen")
        ))

        bl_ps.add_widget(Button(
            text="Thermodynamics",
            on_press=lambda x: self.go_to("thermodynamics_screen")
        ))

        bl_ps.add_widget(Button(
            text="Optics",
            on_press=lambda x: self.go_to("optics_screen")
        ))
        
        bl_ps.add_widget(Button(
            text="<- Назад",
            size_hint=(1, .5),
            on_press=lambda x: setattr(self.manager, "current", "main")
        ))
        
        self.add_widget(bl_ps)

    def go_to(self, screen_name):
        if screen_name in self.manager.screen_names:
            self.manager.current = screen_name
        else:
            print(f"Экран {screen_name} не найден")
