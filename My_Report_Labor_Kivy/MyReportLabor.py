import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class MyReportScreen(Widget):
    pass

class MyReportUI(Widget):
    pass

class MyReportLaborApp(App):
    def build(self):
        return MyReportUI()

MyReportLaborApp().run()