from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# interface
class LogicalInterface(BoxLayout):
    def OnPressing(self):
        print("Hello world")
    
    def OnReleasing(self):
        print("YOOOOOO")

# app creation
class TestApp(App):
    pass

TestApp().run()