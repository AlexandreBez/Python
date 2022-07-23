from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

# interface
class Interface(FloatLayout):
    layout=BoxLayout()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1=Button(text="hello", size_hint=(.25, .25), pos=(200,100), pos_hint={})
        self.layout.add_widget(b1)
        self.add_widget(self.layout)

# app creation
class TestApp(App):
    pass

TestApp().run()