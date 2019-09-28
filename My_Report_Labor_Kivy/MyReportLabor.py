from kivy.app import App
from kivy.uix.label import Label


class MyReportLabor(App):
    def build(self):
        return Label(text='Hello World!')

MyReportLabor().run()