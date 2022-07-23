from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# interface
# Builder.load_file("BuilderOther.kv")
Builder.load_string("""
<ExternalKivy>:
    Button:
        text: "Hello"
""")
class ExternalKivy(BoxLayout):
    pass

class Variables(BoxLayout):
    _text_ = StringProperty("Hello world")
    def pressing(self, btn):
        self._text_ = "Welcome"
        btn.text = "We have changed this text with help of self"

class LogicalInterface(BoxLayout):
    def OnPressing(self, ID, input):
        print("Hello world")
        ID.text = input.text
    
    def OnReleasing(self, ID, input):
        print("YOOOOOO")
        ID.text = input.text

# app creation
class TestApp(App):
    def Build(self):
        return ExternalKivy()

TestApp().run()