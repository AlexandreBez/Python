from kivy.app import App
from kivy.uix.widget import Widget

# interface
class Interface(Widget):
    def On_Enter_Pressed(self):
        print("YOOOOOOOOOOOOOOOOOOOOOOO")

# app creation
class TestApp(App):
    pass

TestApp().run()