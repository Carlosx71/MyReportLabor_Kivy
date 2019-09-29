from kivy.app import App
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Layout(BoxLayout):
    pass

class MyReportLabor(App):
    def build(self):
        return Layout()
        #return Label(text='Hello World!')
        #anim = Animation(x=100, y=100)
        #anim.start(widget)

MyReportLabor().run()