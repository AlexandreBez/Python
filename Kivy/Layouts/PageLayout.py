from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout

# interface
class Page_Layout(PageLayout):
    pass

class Page_1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1=Button(text="Hello")
        b2=Button(text="World")
        self.add_widget(b1)
        self.add_widget(b2)

class Page_2(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1=Button(text="Hello")
        b2=Button(text="World")
        self.add_widget(b1)
        self.add_widget(b2)

class Page_3(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1=Button(text="Hello")
        b2=Button(text="World")
        self.add_widget(b1)
        self.add_widget(b2)

class Relative_Practice(FloatLayout):
    pass

class Interface(FloatLayout):
    pass

class scroller(ScrollView):
    pass

class stackinterface(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(30):
            b1=Button(text="1", size_hint=(.15,.15), background_color=(i*0.1,i*0.1,i*0.1,i*0.1))
            self.add_widget(b1)

# app creation
class TestApp(App):
    pass

TestApp().run()