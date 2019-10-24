#from win10toast import ToastNotifier 
from datetime import timedelta, date
from threading import Thread
import http.client, urllib.parse
import datetime
import base64
import requests
import json
import os
import kivy
import time
from kivy.app               import App
from kivy.uix.label         import Label
from kivy.animation         import Animation
from kivy.uix.button        import Button
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.textinput     import TextInput
from kivy.uix.widget        import Widget
from kivy.uix.gridlayout    import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image         import Image
from kivy.properties        import ObjectProperty, StringProperty
from kivy.uix.accordion     import Accordion, AccordionItem
from kivy.uix.stacklayout   import StackLayout

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
    #def changeScreen(self):
    #    myreportswscreen = self.manager.ids.MyReportSWScreen
    #    self.manager.current = 'MyReportSWScreen'
    #    #self.bind(on_press=self.myreportswscreen.transTela)
    def transTela(self, *args):
        self.manager.current = 'MyReportLoginScreen'    

    def login(self):
        #print(str(username) + str(password))
        print('Entrou no Login')
        usuario = self.username.text
        senha = self.password.text
        #noencoder_maxauth= usuario+':'+senha
        #encoder_maxauth = base64.b64encode(noencoder_maxauth.encode())
        #url = self.servidor+"/maximo/rest/mbo/PERSON/"
        #querystring = {"personid":usuario,"_format":"json"}
        #conn = http.client.HTTPConnection(self.servidor)
        #payload = ""
        #senha = str(encoder_maxauth)
        #print(senha[1:])
        #headers = {
        #   'maxauth': senha[1:],
        #   'cache-control': "no-cache",
        #   'Postman-Token': "7d953751-3549-4a4c-b943-c8b09266463e"
        #   }
        #print('Chegou no headers')
        #conn.request("GET", self.urlHttp+"/maximo/rest/mbo/PERSON?_format=json&personid="+usuario, payload, headers)
        #res = conn.getresponse()
        #data = res.read()
        #print(data.decode("utf-8"))
        #response = data.decode("utf-8")
        #if response[:21] == "Error 400: BMXAA7901E":
        #	print("ERRO......")
        #else:
        #self.changeScreen()
        myreportswscreen = self.manager.ids.MyReportSWScreen
        self.manager.current = 'MyReportSWScreen'
        #MyReportSWScreen.listSRandWO(self)
    #    #self.bind(on_press=self.myreportswscreen.transTela)



    #def load(self, pessoa):
    #    #Instaciando a tela para navegacao buscando no arquivo KV
    #    myreportswscreen = self.manager.ids.MyReportSWScreen
    #    #Pega a lista do jsonRest
    #    jsonPessoa = JsonRestMaximo.jsonRest
    #    if pessoa == 'Carlos':
    #        for x, i in jsonPessoa[0]['Carlos'].items():
    #            #Cria um botao de acordo com o discionario de dados. O box1 e um id que esta no arquivo KV
    #            self.ids.box1.add_widget(MyButton(myreportswscreen, i['nome'], i['idade']))
    #            print(str(x))
    #            print(str(i))
    #    elif pessoa == 'Veronica':
    #        for x, i in jsonPessoa[1]['Veronica'].items():
    #            #Cria um botao de acordo com o discionario de dados. O box1 e um id que esta no arquivo KV
    #            self.ids.box1.add_widget(MyButton(myreportswscreen, i['nome'], i['idade']))
    #            print(str(x))
    #            print(str(i))

class MyButton(Button):
    def __init__(self,screen, nome, idade,num, **kwargs):
        super(MyButton, self).__init__(**kwargs)

        #Construindo o botao
        self.id = 'buttonList'+num
        self.text = nome
        self.size_hint_y = None
        self.width = self.width * 0.500
        self.height = '50dp'
        self.background_color = 255,255,255,1
        self.color = 0,0,0,1
        self.background_normal
        #Amarra para tela MyReportSWScreen
        self.screen = screen
        #self.screens1 = screen
        self.bind(on_press=self.screen.transTelaWOScreen)

        #woscreen = self.manager.ids.WOScreen
        #self.manager.current = 'WOScreen'

class MyButton(Button):
    def __init__(self,screen, nome, idade,num, **kwargs):
        super(MyButton, self).__init__(**kwargs)

        #Construindo o botao
        self.id = 'buttonList'+num
        self.text = nome
        self.size_hint_y = None
        self.width = self.width * 0.500
        self.height = '50dp'
        self.background_color = 255,255,255,1
        self.color = 0,0,0,1
        self.background_normal
        #Amarra para tela MyReportSWScreen
        self.screen = screen
        #self.screens1 = screen
        self.bind(on_press=self.screen.transTelaWOScreen)

class MyButtonWO(Button):
    def __init__(self,screen, nome, idade,num, **kwargs):
        super(MyButtonWO, self).__init__(**kwargs)

        #Construindo o botao
        self.id = 'buttonList'+num
        self.text = nome
        self.size_hint_y = None
        self.width = self.width * 0.500
        self.height = '50dp'
        self.background_color = 255,255,255,1
        self.color = 0,0,0,1
        #self.background_normal
        #Amarra para tela MyReportSWScreen
        self.screen = screen
        #self.screens1 = screen
        self.bind(on_press=self.screen.transTelaWOScreen)
        self.bind(on_press=self.screen.teste)


class MyReportSWScreen(Screen):
    num = 0
    btn = ObjectProperty(None)
    def transTela(self, *args):
        self.manager.current = 'WOScreen'

    def count(self):
        pass
    def listSRandWO(self):
        woScreen = self.manager.ids.WOScreen
        print('listSRandWO')
        jsonPessoa = JsonRestMaximo.jsonRest
        self.num = self.num + 1
        for x, i in jsonPessoa[0]['Carlos'].items():
        #Cria um botao de acordo com o discionario de dados. O box1 e um id que esta no arquivo KV
            if self.num == 1:
                self.ids.boxSRWO.add_widget(MyButtonWO(woScreen, i['nome'], i['idade'], str(self.num)))
                print(str(x))
                print(str(i))
            else:
                self.ids.boxSRWO.remove_widget(MyButtonWO(woScreen, i['nome'], i['idade'], str(self.num)))
        print(self.num)
        #noencoder_maxauth=usuario+':'+senha
        #encoder_maxauth = base64.b64encode(noencoder_maxauth.encode())
        #laborcode = self.recuperaLabor()
        ##url = self.sevidor+"/maximo/rest/mbo/WPLABOR/?_format=json&laborcode="+laborcode
        #url = self.urlHttp+"/maximo/oslc/script/MAXINSTWORKITENS_SR"
        #querystring = ""
        #conn = http.client.HTTPConnection(self.servidor)
        #payload = ""
        #senha = str(encoder_maxauth)
        #print(senha[1:])
        #headers = {
        #   'maxauth': senha[1:],
        #   'cache-control': "no-cache",
        #   'Postman-Token': "7d953751-3549-4a4c-b943-c8b09266463e"
        #   }
        #print(headers)
        #print(url)       
        #conn.request("GET", self.urlHttp+"/maximo/oslc/script/MAXINSTWORKITENS_SR?_format=json", payload, headers)
        #res = conn.getresponse()
        #data = res.read()
        #print('\033[32m '+data.decode("utf-8")+' \033[m')	
        #response = data.decode("utf-8")	
        ##binary = response.text
        #jsonToPython = json.loads(response)
        #self.workitens_sr_des = json.loads(response)
        #'''
        #text = '{"data": [{"description": "Workitem Maxinst para Reuni","workitem": "MAX0REUNI"},{"description": "Tarefa Teste","taskid": "10","workitem": "MAX0TESTE"},{"description": "teste da OS de workitem","workitem": "MAX0PROJET"},{"description": "MAXTESTEAPONT","workitem": "MAX0TESTE"}]}'
        #jsonToPython = json.loads(text)
        #self.workitens_sr_des = json.loads(text)
        #'''
        
        #workitens_sr_descricao = '{"'
        #workitens = '{"workitens":["'
        #for wplabor in jsonToPython["data"]:
        #	wpdescription = wplabor.get('description')
        #	wpdescription=wpdescription.replace('"','')
        #	wpdescription=wpdescription.replace("'","")
        #	workitemdesc=wplabor.get('workitem')
        #	workitemdesc = workitemdesc.replace('"','')
        #	workitemdesc = workitemdesc.replace("'","")
        #	workitens = workitens + workitemdesc + '","'
        #	workitens_sr_descricao = workitens_sr_descricao + wplabor.get('workitem')  +'":"' +  wpdescription + '","'
        #
        #if workitens != '{"workitens":["':
        #	workitens=workitens[:-2]
        #	workitens=workitens+']}'
        #	workitens_sr_descricao=workitens_sr_descricao[:-2]
        #	workitens_sr_descricao=workitens_sr_descricao+'}'
        #	self.workitens_sr_des = json.loads(workitens_sr_descricao)
        #	return workitens
        #else:
        #	return None
class WOScreen(Screen):
    def transTelaWOScreen(self, *args):
        self.manager.current = 'WOScreen'

    def teste(self, *args):
        print('To na WoScreen')

class MyReportLaborApp(App):
    def build(self):
        return MyReportScreen()

MyReportLaborApp(kv_file='MyReportLabor.kv').run()