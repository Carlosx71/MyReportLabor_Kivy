import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager

class JsonRestMaximo():
    jsonRest = [{'Carlos':{
                    'Heroi 1': {
                        'nome':'Dante', 
                        'idade': 25,
                        'cabelos': 'Brancos'
                        }, 
                    'Heroi 2': {
                        'nome':'Kenshin', 
                        'idade': 27,
                        'cabelos': 'Negros'
                        }                
                    }
                },
                {'Veronica':{
                    'Heroi 1': {
                        'nome':'Alice', 
                        'idade': 22,
                        'cabelos': 'Castanhos'
                        }, 
                    'Heroi 2': {
                        'nome':'Aru', 
                        'idade': 20,
                        'cabelos': 'Loiros'
                        }                
                    }
                },                
                ]

class MyReportScreen(ScreenManager):
    pass

class MyReportLoginScreen(Screen):
    def load(self, pessoa):
        #Instaciando a tela para navegacao buscando no arquivo KV
        myreportswscreen = self.manager.ids.MyReportSWScreen
        #Pega a lista do jsonRest
        jsonPessoa = JsonRestMaximo.jsonRest
        if pessoa == 'Carlos':
            for x, i in jsonPessoa[0]['Carlos'].items():
                #Cria um botao de acordo com o discionario de dados. O box1 e um id que esta no arquivo KV
                self.ids.box1.add_widget(MyButton(myreportswscreen, i['nome'], i['idade']))
                print(str(x))
                print(str(i))
        elif pessoa == 'Veronica':
            for x, i in jsonPessoa[1]['Veronica'].items():
                #Cria um botao de acordo com o discionario de dados. O box1 e um id que esta no arquivo KV
                self.ids.box1.add_widget(MyButton(myreportswscreen, i['nome'], i['idade']))
                print(str(x))
                print(str(i))

class MyButton(Button):
    def __init__(self,myreportswscreen, nome, idade, **kwargs):
        super(MyButton, self).__init__(**kwargs)

        self.text = nome
        self.size_hint_y = None
        self.height = '300dp'

        #Amarra para tela MyReportSWScreen
        self.myreportswscreen = myreportswscreen
        self.bind(on_press=self.myreportswscreen.transTela)

class MyReportSWScreen(Screen):
        def transTela(self, *args):
            self.manager.current = 'MyReportSWScreen'

class MyReportLaborApp(App):
    def build(self):
        return MyReportScreen()

MyReportLaborApp().run()