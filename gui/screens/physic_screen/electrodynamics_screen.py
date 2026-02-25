from cProfile import label
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class ElectrodynamicsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
# Create Layouts
        bl_elds = BoxLayout(orientation="vertical", spacing=20, padding=40)
        gl_elds = GridLayout(cols=1, spacing = 10, size_hint_y=None, padding=40)
        gl_elds.bind(minimum_height=gl_elds.setter('height'))
    
# Create and add label
        label = Label(
            text="Выберите раздел",
            font_size=32,
            size_hint=(1, .2),
        )
        
# Create and add buttons
    #ЗАКОН КУЛОНА
        gl_elds.add_widget(Button(
            text="Закон Кулона",
            size_hint_y = None,
        ))
    #НАПРЯЖЕННОСТЬ ЭЛЕКТРИЧЕСКОГО ПОЛЯ
        gl_elds.add_widget(Button(
            text="Напряженность электрического поля",
            size_hint_y = None,
        ))
    #НАПРЯЖЕННОСТЬ ЭЛЕКТРИЧЕСКОГО ПОЛЯ ТОЧЕЧНОГО ЗАРЯДА
        gl_elds.add_widget(Button(
            text="Напряженность электрического поля точечного заряда",
            size_hint_y = None,
        ))
    #ПОВЕРХНОСТНАЯ ПЛОТНОСТЬ ЗАРЯДА
        gl_elds.add_widget(Button(
            text="Поверхностная плотность заряда",
            size_hint_y = None,
        ))
    #НАПРЯЖЕННОСТЬ ЭЛЕКТРИЧЕСКОГО ПОЛЯ БЕСКОНЕЧНОЙ ПЛОСКОСТИ    
        gl_elds.add_widget(Button(
            text="Напряженность электрического поля бесконечной плоскости",
            size_hint_y = None,
        ))
    #ДИЭЛЕКТРИЧЕСКАЯ ПОСТОЯННАЯ   
        gl_elds.add_widget(Button(
            text = "Диэлектрическая постоянная",
            size_hint_y = None,
        ))
    #ПОТЕНЦИАЛЬНАЯ ЭНЕРГИЯ ВЗАИМОДЕЙСТВИЯ ЗАРЯДОВ       
        gl_elds.add_widget(Button(
            text = "Потенциальная энергия взаимодействия зарядов",
            size_hint_y = None,
        ))
    #ПОТЕНЦИАЛЬНАЯ ЭНЕРГИЯ ВЗАИМОДЕЙСТВИЯ ЗАРЯДОВ    
        gl_elds.add_widget(Button(
            text = "Потенциал",
            size_hint_y = None,
        ))
    #ПОТЕНЦИАЛЬНАЯ ЭНЕРГИЯ ВЗАИМОДЕЙСТВИЯ ЗАРЯДОВ    
        gl_elds.add_widget(Button(
            text = "Потенциал точечного заряда",
            size_hint_y = None,
        ))
    #НАПРЯЖЕНИЕ   
        gl_elds.add_widget(Button(
            text = "Напряжение",
            size_hint_y = None,
        ))
    #НАПРЯЖЕНИЕ ЭЛЕКТРИЧЕСКОГО ПОЛЯ   
        gl_elds.add_widget(Button(
            text = "Напряжение электрического поля",
            size_hint_y = None,
        ))
    #ЭЛЕКТРИЧЕСКАЯ ЕМКОСТЬ    
        gl_elds.add_widget(Button(
            text = "Электрическая емкость",
            size_hint_y = None,
        ))
    #ЭЛЕКТРИЧЕСКАЯ ЕМКОСТЬ ПЛОСКОГО КОНДЕНСАТОРА    
        gl_elds.add_widget(Button(
            text = "Электрическая емкость плоского конденсатора",
            size_hint_y = None,
        ))
    #СИЛА ТОКА    
        gl_elds.add_widget(Button(
            text = "Сила тока",
            size_hint_y = None,
        ))
    #СОПРОТИВЛЕНИЕ ПРОВОДНИКА    
        gl_elds.add_widget(Button(
            text = "Сопротивление проводника",
            size_hint_y = None,
        ))
    #ЗАКОН ОМА ДЛЯ УЧАСТКА ЦЕПИ    
        gl_elds.add_widget(Button(
            text = "Закон Ома для участка цепи",
            size_hint_y = None,
        ))
    #МОЩНОСТЬ ЭЛЕКТРИЧЕСКОГО ТОКА    
        gl_elds.add_widget(Button(
            text = "Мощность электрического тока",
            size_hint_y = None,
        ))
    #ЗАКОН ДЖОУЛЯ-ЛЕНЦА    
        gl_elds.add_widget(Button(
            text = "Закон Джоуля-Ленца",
            size_hint_y = None,
        ))
    #ЗАКОН ОМА ДЛЯ ПОЛНОЙ ЦЕПИ    
        gl_elds.add_widget(Button(
            text = "Закон Ома для полной цепи",
            size_hint_y = None,
        ))
    #СИЛА ТОКА КОРОТКОГО ЗАМЫКАНИЯ    
        gl_elds.add_widget(Button(
            text = "Сила тока короткого замыкания",
            size_hint_y = None,
        ))
    #ВЕКТОР МАГНИТНОЙ ИНДУКЦИИ   
        gl_elds.add_widget(Button(
            text = "Вектор магнитной индукции",
            size_hint_y = None,
        ))
    #СИЛА АМПЕРА    
        gl_elds.add_widget(Button(
            text = "Сила Ампера",
            size_hint_y = None,
        ))
    #СИЛА ЛОРЕНЦА    
        gl_elds.add_widget(Button(
            text = "Сила Лоренца",
            size_hint_y = None,
        ))
    #МАГНИТНЫЙ ПОТОК    
        gl_elds.add_widget(Button(
            text = "Магнитный поток",
            size_hint_y = None,
        ))
    #ЗАКОН ЭЛЕКТРОМАГНИТНОЙ ИНДУКЦИИ    
        gl_elds.add_widget(Button(
            text = "Закон электромагнитной индукции",
            size_hint_y = None,
        ))
    #ЭДС ДВИЖУЩЕГОСЯ ПРОВОДНИКА    
        gl_elds.add_widget(Button(
            text = "ЭДС движущегося проводника",
            size_hint_y = None,
        ))
    #ЭДС САМОИНДУКЦИИ    
        gl_elds.add_widget(Button(
            text = "ЭДС самоиндукции",
            size_hint_y = None,
        ))
    #ЭНЕРГИЯ МАГНИТНОГО ПОЛЯ КАТУШКИ    
        gl_elds.add_widget(Button(
            text = "Энергия магнитного поля катушки",
            size_hint_y = None,
        ))
    #ПЕРИОД КОЛЕБАНИЙ В КОЛЕБАТЕЛЬНОМ КОНТУРЕ    
        gl_elds.add_widget(Button(
            text = "Период колебаний в колебательном контуре",
            size_hint_y = None,
        ))
    #ИНДУКТИВНОЕ СОПРОТИВЛЕНИЕ   
        gl_elds.add_widget(Button(
            text = "Индуктивное сопротивление",
            size_hint_y = None,
        ))
    #ЕМКОСТНОЕ СОПРОТИВЛЕНИЕ    
        gl_elds.add_widget(Button(
            text = "Емкостное сопротивление",
            size_hint_y = None,
        ))
    #ДЕЙСТВИТЕЛЬНОЕ ЗНАЧЕНИЕ СИЛЫ ТОКА    
        gl_elds.add_widget(Button(
            text = "Действующее значение силы тока",
            size_hint_y = None,
        ))
    #ДЕЙСТВИТЕЛЬНОЕ ЗНАЧЕНИЕ НАПРЯЖЕНИЯ    
        gl_elds.add_widget(Button(
            text = "Действующее значение напряжения",
            size_hint_y = None,
        ))
    #ОБЩЕЕ СОПРОТИВЛЕНИЕ    
        gl_elds.add_widget(Button(
            text = "Общее сопротивление",
            size_hint_y = None,
        ))

#Create ScrollView
        scroll_view = ScrollView(size_hint=(1, 0.8))
        scroll_view.add_widget(gl_elds)
        
 #BACK BUTTON       
        back_button = Button(
            text="<- Назад",
            size_hint=(1, .2),
            on_press=lambda x: setattr(self.manager, "current", "physics_screen")
        )
        
#Add Layouts to BoxLayout
        bl_elds.add_widget(label)
        bl_elds.add_widget(scroll_view)     
        bl_elds.add_widget(back_button)
        self.add_widget(bl_elds)
    
    def go_to(self, screen_name):
        if screen_name in self.manager.screen_names:
            self.manager.current = screen_name
        else:
            print(f"Экран {screen_name} не найден")
            
