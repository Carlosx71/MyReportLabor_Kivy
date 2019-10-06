from win10toast import ToastNotifier 
from datetime import timedelta, date
from threading import Thread
import http.client, urllib.parse
import datetime
import base64
import requests
import json
import os
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
from kivy.uix.image import Image

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

    #self.urlHttp = "http://suportedev.maxinst.intra"
    #self.servidor = "suportedev.maxinst.intra"
    urlHttp = "http://suporte.maxinst.intra"
    servidor = "suporte.maxinst.intra"
    def changeScreen(self):
        myreportswscreen = self.manager.ids.MyReportSWScreen
        self.manager.current = 'MyReportSWScreen'
        #self.bind(on_press=self.myreportswscreen.transTela)
    
    def login(self):
        #username = self.username.text
        #password = self.password.text
        #print(str(username) + str(password))
        print('Entrou no Login')
        usuario = self.username.text
        senha = self.password.text
        noencoder_maxauth= usuario+':'+senha
        encoder_maxauth = base64.b64encode(noencoder_maxauth.encode())
        url = self.servidor+"/maximo/rest/mbo/PERSON/"
        querystring = {"personid":usuario,"_format":"json"}
        conn = http.client.HTTPConnection(self.servidor)
        payload = ""
        senha = str(encoder_maxauth)
        print(senha[1:])
        headers = {
           'maxauth': senha[1:],
           'cache-control': "no-cache",
           'Postman-Token': "7d953751-3549-4a4c-b943-c8b09266463e"
           }
        print('Chegou no headers')
        conn.request("GET", self.urlHttp+"/maximo/rest/mbo/PERSON?_format=json&personid="+usuario, payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        response = data.decode("utf-8")
        if response[:21] == "Error 400: BMXAA7901E":
        	print("ERRO......")
        else:
            self.changeScreen()



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

        #Construindo o botao
        self.text = nome
        self.size_hint_y = None
        self.height = '300dp'

        #Amarra para tela MyReportSWScreen
        self.myreportswscreen = myreportswscreen
        self.bind(on_press=self.myreportswscreen.transTela)

class TextInput(Widget):
    pass

class MyReportSWScreen(Screen):
        def transTela(self, *args):
            self.manager.current = 'MyReportSWScreen'

class MyReportLaborApp(App):
    def build(self):
        return MyReportScreen()

MyReportLaborApp().run()