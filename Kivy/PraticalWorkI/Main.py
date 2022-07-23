from random import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

# Interface

class Game(BoxLayout):
    btn_lst=[]
    i=0
    Alpha=["A","B","C","D","E"]

    def create_btn(self, stacker):
        ALPHA=random.choice(self.Alpha)
        r=random.randrange(1,10)
        g=random.randrange(1,10)
        b=random.randrange(1,10)
        R=r/10
        G=g/10
        B=b/10
        btn=Button(text=str(ALPHA), size_hint=(None,None), size=(100, 100), background_color=(R,G,B,1), background_norma="")
        self.btn_lst.append(btn)
        self.ids.stacker.add_widget(btn)
        self.i=self.i+1
        print("Button Created")
    def remove_btn(self, stacker):
        if self.i>0:
            self.ids.stacker.remove_widget(self.btn_lst[self.i+1])
            self.btn_lst.pop(self.i+1)
            self.i=self.i+1
            print("Button removed")

class Buttons(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            b1=Button(text=str(i+1), size_hint=(None, None), size=(100, 1))
            self.add_widget(b1)
    

# app creation
class TestApp(App):
    pass

TestApp().run()