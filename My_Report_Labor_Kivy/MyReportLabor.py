#from win10toast import ToastNotifier 
from datetime import timedelta, date
from threading import Thread
from collections import defaultdict
from functools import partial
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

class JsonRestMaximo(Screen):
    def jsonGetLabor(self,username, password):
        usuario = username
        senha = password
        noencoder_maxauth = usuario+':'+senha
        encoder_maxauth = base64.b64encode(noencoder_maxauth.encode())
        url = MyReportLoginScreen.urlHttp + "/maximo/rest/mbo/LABOR/"
        querystring = {"personid":usuario,"_format":"json"}
        payload = ""
	    #data = {}
        senha = str(encoder_maxauth)
        print(senha[1:])
        headers = {
           'maxauth': senha[1:],
           'cache-control': "no-cache",
           'Postman-Token': "7d953751-3549-4a4c-b943-c8b09266463e"
           }
        conn = http.client.HTTPConnection("suporte.maxinst.intra")
        conn.request("GET", '/maximo/rest/mbo/LABOR?_format=json&personid="'+usuario+'"', payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        response = data.decode("utf-8")
        jsonToPython = json.loads(response)
        labor = jsonToPython["LABORMboSet"]['LABOR'][0]
        attributes = labor['Attributes']
        print(attributes.get('LABORCODE').get('content'))
        return attributes.get('LABORCODE').get('content')
    
    def jsonWOSR(self, user, passw, labor):
        usuario = user   		
        senha = passw
        noencoder_maxauth = usuario+':'+senha
        encoder_maxauth = base64.b64encode(noencoder_maxauth.encode())
        laborcode = labor
        servidor = MyReportLoginScreen.servidor
        #url = self.sevidor+"/maximo/rest/mbo/WPLABOR/?_format=json&laborcode="+laborcode
        url = servidor+"/maximo/oslc/script/MAXINSTWORKITENS_SR"
        querystring = ""
        conn = http.client.HTTPConnection("suporte.maxinst.intra")
        payload = ""
        senha = str(encoder_maxauth)
        print(senha[1:])
        headers = {
           'maxauth': senha[1:],
           'cache-control': "no-cache",
           'Postman-Token': "7d953751-3549-4a4c-b943-c8b09266463e"
           }
        print(headers)
        print(url)
        conn.request("GET", "http://suporte.maxinst.intra/maximo/oslc/script/MAXINSTWORKITENS_SR?_format=json", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print("\033[33m" + data.decode("utf-8") +"\033[m")	
        response = data.decode("utf-8")	
        jsonToPython = json.loads(response)
        self.workitens_sr_des = json.loads(response)
        '''
        text = '{"data": [{"description": "Workitem Maxinst para Reuni","workitem": "MAX0REUNI"},{"description": "Tarefa Teste","taskid": "10","workitem": "MAX0TESTE"},{"description": "teste da OS de workitem","workitem": "MAX0PROJET"},{"description": "MAXTESTEAPONT","workitem": "MAX0TESTE"}]}'
        jsonToPython = json.loads(text)
        self.workitens_sr_des = json.loads(text)
        '''
        workitens_sr_descricao = '{"'
        workitens = '{"workitens":["'
        for wplabor in jsonToPython["data"]:
        	wpdescription = wplabor.get('description')
        	wpdescription=wpdescription.replace('"','')
        	wpdescription=wpdescription.replace("'","")
        	workitemdesc=wplabor.get('workitem')
        	workitemdesc = workitemdesc.replace('"','')
        	workitemdesc = workitemdesc.replace("'","")
        	workitens = workitens + workitemdesc + '","'
        	workitens_sr_descricao = workitens_sr_descricao + wplabor.get('workitem')  +'":"' +  wpdescription + '","'

        if workitens != '{"workitens":["':
        	workitens=workitens[:-2]
        	workitens=workitens+']}'
        	workitens_sr_descricao=workitens_sr_descricao[:-2]
        	workitens_sr_descricao=workitens_sr_descricao+'}'
        	self.workitens_sr_des = json.loads(workitens_sr_descricao)
        	print("\033[37m"+ workitens + "\033[m")
        	return data
        else:
        	return None
    


class MyReportScreen(ScreenManager):
    pass


class MyReportLoginScreen(Screen):

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
        for key, val in self.ids.items():
            print("key={0}, val={1}".format(key, val))
        usuario = self.username.text
        senha = self.password.text
        password = ''
        password = senha
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
        if  password != '' and usuario != '':
            print('Entrou no if de user')
            conn.request("GET", self.urlHttp+"/maximo/rest/mbo/PERSON?_format=json&personid="+usuario, payload, headers)
            res = conn.getresponse()
            data = res.read()
            print(data.decode("utf-8"))
            response = data.decode("utf-8")
            if response[:21] == "Error 400: BMXAA7901E":
            	print("Usuario ou Senha incorreto")
            else:
            #self.changeScreen()
                myreportswscreen = self.manager.ids.MyReportSWScreen
                self.manager.current = 'MyReportSWScreen'
                JsonRestMaximo.jsonGetLabor(self,usuario, password)
                MyReportSWScreen.usuario = usuario
                MyReportSWScreen.password = password
        else:
            print('Preencha os campos obrigatorios')
        #MyReportSWScreen.listSRandWO(self)

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


class MyButtonWO(Button):
    def __init__(self,screen, workitem, description, num, **kwargs):
        super(MyButtonWO, self).__init__(**kwargs)

        #Construindo o botao
        self.id = 'buttonList'+num
        self.text = workitem
        self.size_hint_y = None
        self.width = self.width * 0.500
        self.height = '50dp'
        self.background_color = 255,255,255,1
        self.color = 0,0,0,1
        #self.background_normal
        #Amarra para tela MyReportSWScreen
        self.screen = screen
        #Callback para chamar a função com parametros
        callback = partial(self.screen.setWO, workitem, description)
        self.bind(on_press=self.screen.transTelaWOScreen)
        self.bind(on_press=callback)


class MyReportSWScreen(Screen):
    num = 0
    usuario = ''
    password = ''
    laborName = ''
    def transTela(self, *args):
        self.manager.current = 'WOScreen'

    def count(self):
        pass

    def listSRandWO(self):
        print("----->>>>> " + self.usuario + " <<<<<------")
        print("----->>>>> " + self.password + " <<<<<------")
        woScreen = self.manager.ids.WOScreen
        print('listSRandWO')
        labor = JsonRestMaximo.jsonGetLabor(self, self.usuario, self.password)
        jsonWOSRstr = JsonRestMaximo.jsonWOSR(self, self.usuario, self.password, labor)
        jsonWOSR = json.loads(jsonWOSRstr)
        self.num = self.num + 1
        for x in jsonWOSR['data']:
            ##Cria um botao de acordo com o discionario de dados. O box1 e um id que esta no arquivo KV
            if self.num == 1:
                self.ids.boxSRWO.add_widget(MyButtonWO(woScreen, x['workitem'], x['description'], str(self.num)))        
                #print(str(i))
            else:
                self.ids.boxSRWO.remove_widget(MyButtonWO(woScreen, x['workitem'], x['description'], str(self.num)))
        print(self.num)

class WOScreen(Screen):
    workitemWO = ''
    descriptionWO = ''

    def transTelaWOScreen(self, *args):
        self.manager.current = 'WOScreen'

    def setWO(self, workitem, description, *args):
        print('To na WoScreen ', str(workitem))
        for key, val in self.ids.items():
            print("key={0}, val={1}".format(key, val))
        self.ids.workOrder.text = workitem
        self.ids.woDesc.text = description
        self.workitemWO = workitem
        self.descriptionWO = description
        print(str(args))

    def startActivity(self):
        print("Start Activity")
        self.iniciot = datetime.datetime.now()
        di = datetime.datetime.now()-timedelta(minutes=1)
        self.inicio_formatada = str(di)
        self.starttime = self.inicio_formatada[self.inicio_formatada.find(' ')+1:self.inicio_formatada.find('.')]
        self.inicio_formatada = self.inicio_formatada.replace(' ','T')
        self.inicio_formatada = self.inicio_formatada[0:self.inicio_formatada.find('.')]
        self.inicio_formatada = self.inicio_formatada + '-03:00'
        self.iniciot=self.iniciot-timedelta(minutes=1)
        self.ids.btnStartAct.disabled = True
	
    def endActivity(self):
        df1 = datetime.datetime.now() - timedelta(minutes=1) 
        fimdata_formatada = str(df1)
        fimdata_formatada = fimdata_formatada.replace(' ','T')
        fimdata_formatada = fimdata_formatada[0:fimdata_formatada.find('.')]
        fimdata_formatada = fimdata_formatada + '-03:00'
        finishtime = fimdata_formatada[fimdata_formatada.find(' ')+1:fimdata_formatada.find('.')]
        finishdate = fimdata_formatada[0:fimdata_formatada.find(' ')]
        print(fimdata_formatada)
        chamado = self.workitemWO
        #chamado = self.listbox.get(self.listbox.curselection())
        #memo = self.memo.get()
        laborcode = JsonRestMaximo.jsonGetLabor(self, MyReportSWScreen.usuario , MyReportSWScreen.password)
        fim = datetime.datetime.now()
        fim = fim - timedelta(minutes=1)
        df = fim - self.iniciot
        print(df)
        dfs = str(df)
        s = dfs.split('.')
        hhmmss = s[0]
        [hours, minutes, seconds] = [int(x) for x in hhmmss.split(':')]
        x = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        segundos=x.seconds
        regularhrs=segundos/3600.0
        print(regularhrs)
        ##result = tkinter.messagebox.askyesno("Confirmacao","Confirma que gastou "+ str(df) + " no chamado\workitem "+str(chamado)+"?")
        ###result = tkMessageBox.askyesno("Confirmacao","Confirma que gastou "+ str(df) + " no chamado\workitem "+str(chamado)+"?")
        #print("language => " +self.language)
        #if self.language == 'EN':
        #	hrstr =str(regularhrs)
        #else:
        hrstr=str(regularhrs)
        #	hrstr = hrstr.replace('.',',')
        #egularhrs=1
        url = "http://suporte.maxinst.intra/maximo/rest/mbo/LABTRANS/"
        ################ --------------- >>>>> VERIFICAR QUANDO FOR SR <<<<< ---------------------- ####################
        #if chamado[:2] == 'SR':
        #	querystring = {"_action":"AddChange","LABORCODE":laborcode,"REGULARHRS":hrstr,"ticketid":chamado,"ticketclass":"SR","siteid":"SEDE","memo":memo,"STARTDATETIME":self.inicio_formatada,"FINISHDATETIME":fimdata_formatada,"STARTTIME":self.starttime}
        querystring = {
            "_action":"AddChange",
            "LABORCODE":laborcode,
            "REGULARHRS":hrstr,
            "refwo":chamado,
            "siteid":"SEDE",
            "memo":"memo",
            "STARTDATETIME":self.inicio_formatada,
            "FINISHDATETIME":fimdata_formatada,
            "STARTTIME":self.starttime
        }
        noencoder_maxauth = MyReportSWScreen.usuario +':'+ MyReportSWScreen.password
        encoder_maxauth = base64.b64encode(noencoder_maxauth.encode())
        payload = ""
        headers = '{"maxauth":"Y2FybG9zLnNhbnRvczpjaG9iaXRz"}'
        print(encoder_maxauth)
        print(querystring)
        h = json.loads(headers)
        response = requests.request("POST", url, data=payload, headers=h, params=querystring)
        print(response.text)
        print(response.status_code)
        self.ids.btnStartAct.disabled = False
        #if (response.status_code == 200):
        #	tkinter.messagebox.showinfo("Sucesso", "Registro gravado com sucesso!!!")
        #else:
        #	tkinter.messagebox.showerror ("Erro", "Não foi possivel gravar os dados no MAXIMO no momento!")

        #print (result)



class MyReportLaborApp(App):
    def build(self):
        return MyReportScreen()

MyReportLaborApp(kv_file='MyReportLabor.kv').run()