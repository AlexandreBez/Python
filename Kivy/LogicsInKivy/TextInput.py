from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# interface
class LogicalInterface(BoxLayout):
    def OnPressing(self, ID, input):
        print("Hello world")
        ID.text = input.text
    
    def OnReleasing(self, ID, input):
        print("YOOOOOO")
        ID.text = input.text

# app creation
class TestApp(App):
    pass

TestApp().run()