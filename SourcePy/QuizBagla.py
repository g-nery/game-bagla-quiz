from pickle import FALSE
import PyQt5
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
sys.path.append('./WindowTemplate/')

from PrimeiraTela import *
from SegundaTela import *
from TerceiraTela import *
from QuartaTela import *
from UltimaTela import *

from win32api import GetSystemMetrics
import json

import subprocess
import os, errno

import win32evtlogutil
import win32evtlog
import time

import random
class Display:
    currentWindow = 0

    def getWidth(self):
        return GetSystemMetrics(0)

    def getHeight(self):
        return GetSystemMetrics(1)
    
    def setCurrentWindow(self, newValue):
        Display.currentWindow = newValue
        
    def getCurrentWindow(self):
        return Display.currentWindow

def createEvent():
    EVT_APP_NAME = "persistWindow"
    EVT_ID = 7040  # Got this from another event
    EVT_CATEG = 9876
    EVT_STRS = ["persistWindow event string {0:d}".format(item) for item in range(5)]
    EVT_DATA = b"persistWindow event data"
    win32evtlogutil.ReportEvent(
                                EVT_APP_NAME, EVT_ID, 
                                eventCategory=EVT_CATEG,
                                eventType=win32evtlog.EVENTLOG_WARNING_TYPE, 
                                strings=EVT_STRS,
                                data=EVT_DATA
                                )       

class Common:
    def __init__(self):

        self.shortcut = QShortcut(QKeySequence("Ctrl+B"), self)
        self.shortcut.activated.connect(self._close)

    @QtCore.pyqtSlot()
    def _close(self):
        sys.exit(app.exec_())

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:
                minimizadas = self.dadosJson.getMinimizadas()
                self.dadosJson.minimizou()
                if(minimizadas > 2):
                    self.m = MessageBox(self, self.dadosJson,"OLOQUINHO MEU", "Você é o rei das minimizadas! Já foram {} tentativas e contando!".format(minimizadas))
                else:
                    self.m = MessageBox(self, self.dadosJson,"AHA!", "Bela Tentativa! Mas ainda assim não será possível ignorar essa tela")

    def configureWindow(self, closeButton = True, minimizeButton = True, frameless = False ):

        if (closeButton == True):
            closeButton = QtCore.Qt.WindowCloseButtonHint
        else:
            closeButton = QtCore.Qt.Window 
    
        if (minimizeButton == True):
            minimizeButton = QtCore.Qt.WindowMinimizeButtonHint
        else:
            minimizeButton = QtCore.Qt.Window 

        if(frameless == True):
            frameless = QtCore.Qt.FramelessWindowHint
        else:
            frameless = QtCore.Qt.Window 

        self.setWindowFlags(
            QtCore.Qt.Window 
        |   frameless
        |   QtCore.Qt.CustomizeWindowHint 
        |   QtCore.Qt.WindowTitleHint
        # |   QtCore.Qt.WindowMaximizeButtonHint
        |   minimizeButton
        |   closeButton
        |   QtCore.Qt.WindowStaysOnTopHint  
            )

    def closeEvent(self, event):  
        self.dadosJson.save()
        createEvent()
        sys.exit(app.exec_())

    def moveEvent(self, e):
        sizeX = self.frameGeometry().width()
        sizeY = self.frameGeometry().height()

        monitor = Display()
        x = int((monitor.getWidth() - sizeX)/2)
        y = int((monitor.getHeight() - sizeY)/2)
        
        self.move(x, y)

class DadosJSON:
    def __init__(self):
        # os.environ.get('LOCALAPPDATA') +
        self.FOLDER_JSON = 'PersistWindow\\'
        self.NAMEFILE_JSON = 'Data.cfg'
        self.PATH_JSON = self.FOLDER_JSON + self.NAMEFILE_JSON 
        
        self.tentativas = None
        if(self._verificaExistsJson() == False):
            self._criarPasta_Saves()

    def _verificaExistsJson(self):
        self.jsonDados = {}
        if os.path.exists(self.PATH_JSON):
            file = open(self.PATH_JSON, "r")
            self.jsonString = file.read()
            self.jsonDados = json.loads(self.jsonString)
            self.tentativas = self.jsonDados["tentativas"]
            self.escondidas = self.jsonDados["escondidas"]
            self.minimizadas = self.jsonDados["minimizadas"]
            return True
        else:
            self.tentativas = 0
            self.escondidas = 0
            self.minimizadas = 0
            return False

    def getTentativas(self):
        return(self.tentativas)

    def getEscondidas(self):
        return(self.escondidas)
    
    def getMinimizadas(self):
        return(self.minimizadas)

    def save(self):
        self.jsonDados = {}
        self.jsonDados["tentativas"] = self.tentativas + 1
        self.jsonDados["escondidas"] = self.escondidas
        self.jsonDados["minimizadas"] = self.minimizadas
        self.jsonString = json.dumps(self.jsonDados)
        #Tenta criar a pasta onde ficara o JSON
        pastaCriada_Saves = self._criarPasta_Saves()
        
        try:
            os.makedirs(self.FOLDER_JSON)
        except:
            pass
        
        try:
            file = open(self.PATH_JSON, "w")
            file.write(self.jsonString)
            file.close()
        except:
            pass
    
    def minimizou(self):
        self.minimizadas += 1

    def escondeu(self):
        self.escondidas += 1

    def _criarPasta_Saves(self):
        FILE_ATTRIBUTE_HIDDEN = 0x02
        try:
            os.makedirs(self.FOLDER_JSON)
        except OSError as e:
            if e.errno != errno.EEXIST:
                return True
            else:
                return True
        else: 
            # ctypes.windll.kernel32.SetFileAttributesW(self.FOLDER_JSON, FILE_ATTRIBUTE_HIDDEN)
            return True


class Janelas(QWidget,Common):
    def __init__(self, **kwargs):
        super().__init__()
        self.display = Display()
        
    def proximaTela(self):
        janelaEmExecucao = self.display.getCurrentWindow()
        janelaEmExecucao += 1
        self.display.setCurrentWindow(janelaEmExecucao)

        self.desenharJanela(janelaEmExecucao)

    def desenharJanela(self, numeroJanela):
        if(numeroJanela == 1):
            self.janela = PrimeiraJanela()
            self.janela.show()
        
        if(numeroJanela == 2):
            self.janela = SegundaTela()
            self.janela.show()

        if(numeroJanela == 3):
            self.janela = TerceiraTela()
            self.janela.show()
        
        if(numeroJanela == 4):
            self.janela = TerceiraTela()
            self.janela.alteraPergunta(str(numeroJanela-2), "Qual dia morreu Teobaldo III de Champanhe?")
            self.janela.alteraOpcoes("Bagla", "13 de maio de 1179", "24 de maio de 1201", "Quem se importa?", "24 de maio de 1201")
            self.janela.show()
        
        if(numeroJanela == 5):
            self.janela = TerceiraTela()
            self.janela.alteraPergunta(str(numeroJanela-2), "1 + 4 = 5\n2 + 5 = 12\n 3 + 6 = 21 \n 8 + 11 = ?")
            self.janela.alteraOpcoes("96", "Bagla", "40", "?", "?")
            self.janela.show()

        if(numeroJanela == 6):
            self.janela = TerceiraTela()
            titulo = str(numeroJanela-2)
            self.janela.alteraPergunta(titulo, "1 + 4 = 10\n2 + 5 = 24\n 3 + 6 = 42 \n 8 + 11 = ?")
            seed = DadosJSON().getTentativas()
            random.seed(seed)
            opcaoCerta = str(random.randrange(1,120))
            opcao1 = str(random.randrange(1,120))
            opcao2 = str(random.randrange(1,120))
            opcao3 = str(random.randrange(1,120))
            self.janela.alteraOpcoes(opcao2, opcao1, opcaoCerta, opcao3, opcaoCerta)
            self.janela.show()

        if(numeroJanela == 7):
            self.janela = TerceiraTela()
            self.janela.alteraPergunta(str(numeroJanela-2), "Qual o nome do funcionário da Blink\nque ligou para o Adler?")
            self.janela.alteraOpcoes("Cesar", "Cleiton", "Rogério", "Felipe", "Cleiton")
            self.janela.show()

        if(numeroJanela == 8):
            self.janela = TerceiraTela()
            self.janela.alteraPergunta(str(numeroJanela-2), "Você aceitaria assinar o seguro\n PET da Blink para si mesmo? (Au au)")
            self.janela.alteraOpcoes("Sim, pagando R$499 mensal", "Sim, com combo junto com o cartão pre-pago e chip 3G", "Não", "Não, porque moro na rua MC Donalds", "Sim, pagando R$499 mensal")
            self.janela.show()

        if(numeroJanela == 9):
            self.janela = QuartaTela()
            self.janela.alteraTitulo(str(numeroJanela-2))
            self.janela.show()

        if(numeroJanela == 10):
            self.janela = UltimaTela()
            self.janela.show()


class PrimeiraJanela(QWidget,Common):

    def __init__(self):
        super().__init__()
        self.dadosJson = DadosJSON()
        self.ui = Ui_JanelaInicial()
        self.ui.setupUi(self)
        
        self.ordemJanelas = Janelas()
        self.configureWindow(closeButton=True)
        
        self.tentativas = self.dadosJson.getTentativas()
        self.ui.botaoNao.clicked.connect(self.acaoBotaoNao)
        self.ui.botaoSim.clicked.connect(self.acaoBotaoSim)
        if(self.tentativas>0):
            self.ui.labelTentativas.setText("Numero de tentativas {}".format(self.tentativas))
        else:
            self.ui.labelTentativas.setText("")
        if(self.tentativas>5):
            self.ui.labelTexto.setText("Você anda fazendo muitas tentativas de fechar o programa, vou desativar o 'x' para ver se ajuda\n\n Você ainda consegue me fechar? ")
            self.configureWindow(closeButton=False)
    @QtCore.pyqtSlot()
    def acaoBotaoNao(self):
        self.m = MessageBox(self, self.dadosJson,"É isso ai", "Boa garoto! Toma um biscoito, au au!", prosseguir=True)

    @QtCore.pyqtSlot()
    def acaoBotaoSim(self):
        self.m = MessageBox(self, self.dadosJson,"ATENÇÃO", "Você foi punido por excesso de confiança. Volte duas casas")

class SegundaTela(QWidget,Common):

    def __init__(self):
        super().__init__()
        self.dadosJson = DadosJSON()
        self.ui = Ui_SegundaJanela()
        self.ui.setupUi(self)
        self.configureWindow(closeButton=False)
        self.ui.botaoSim.clicked.connect(self.acaoBotaoSim)

    @QtCore.pyqtSlot()
    def acaoBotaoSim(self):
        self.m = MessageBox(self, self.dadosJson,"Vamos iniciar", "Agora o Puzzle vai começar então!", prosseguir=True)

class TerceiraTela(QWidget, Common):
    def __init__(self):
        super().__init__()
        self.dadosJson = DadosJSON()
        self.ordemJanelas = Janelas()
        self.ui = Ui_TerceiraJanela()
        self.ui.setupUi(self)
        self.configureWindow(closeButton=False)
        self.opcaoCorreta = "Ele não falou nada nesse video"

        self.ui.labelTexto.setFont(QFont('Times', 12))
        self.ui.labelTitulo.setFont(QFont('Times', 16))
        
        self.ui.labelTitulo.setText("Pergunta 1 / 145")
        self.ui.labelTexto.setText("Qual é a primeira palavra que \n o Filipe Neto disse em seu primeiro \nvideo no Youtube?")

        self.ui.botaoOpcao1.clicked.connect(self.acaoBotao1)
        self.ui.botaoOpcao2.clicked.connect(self.acaoBotao2)
        self.ui.botaoOpcao3.clicked.connect(self.acaoBotao3)
        self.ui.botaoOpcao4.clicked.connect(self.acaoBotao4)


    @QtCore.pyqtSlot()
    def acaoBotao1(self):
        escolhido = self.ui.botaoOpcao1.text()
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotao2(self):
        escolhido = self.ui.botaoOpcao2.text()
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotao3(self):
        escolhido = self.ui.botaoOpcao3.text()
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotao4(self):
        escolhido = self.ui.botaoOpcao4.text()
        self.verificaCorreta(escolhido)

    def alteraPergunta(self, titulo = "", corpo = ""):
        self.ui.labelTitulo.setText("Pergunta {} / 145".format(titulo))
        self.ui.labelTexto.setText(corpo)
        
    
    def alteraOpcoes(self, opcao1="", opcao2="", opcao3="", opcao4="", correta=""):
        self.ui.botaoOpcao1.setText(opcao1)
        self.ui.botaoOpcao2.setText(opcao2)
        self.ui.botaoOpcao3.setText(opcao3)
        self.ui.botaoOpcao4.setText(opcao4)
        self.opcaoCorreta = correta

    def verificaCorreta(self, escolha):
        if(escolha == self.opcaoCorreta):
            self.m = self.ordemJanelas.proximaTela()
            self.hide()
        elif(escolha == "Sim, com combo junto com o cartão pre-pago e chip 3G"):
            self.m = MessageBox(self, self.dadosJson,"OCORREU UM EQUIVOCO", "Perdão, essa promoção acabou. Tente novamente", prosseguir=False)
        else:
            self.m = MessageBox(self, self.dadosJson,"ERROOOU", "Você tomou o penetrex do Andrex!", prosseguir=False)
            self.hide()

class QuartaTela(QWidget, Common):
    def __init__(self):
        super().__init__()
        self.dadosJson = DadosJSON()
        self.ordemJanelas = Janelas()
        self.ui = Ui_QuartaJanela()
        self.ui.setupUi(self)
        self.configureWindow(closeButton=False)

        self.opcaoCorreta = ['A','L','G','A','B']
        self.listaDeCliques = ["","","","",""]

        self.numCliques = 0
        self.ui.labelTexto.setFont(QFont('Times', 12))
        self.ui.labelTitulo.setFont(QFont('Times', 16))
        
        self.ui.labelTitulo.setText("Pergunta 1 / 145")
        self.ui.labelTexto.setText("Qual o nome da primeira pessoa a \njogar Minecraft na Arabia Saudita?")
        self.ui.botaoPular.hide()

        self.ui.opcaoA.clicked.connect(self.acaoBotaoA)
        self.ui.opcaoB.clicked.connect(self.acaoBotaoB)
        self.ui.opcaoC.clicked.connect(self.acaoBotaoC)
        self.ui.opcaoD.clicked.connect(self.acaoBotaoD)
        self.ui.opcaoE.clicked.connect(self.acaoBotaoE)
        self.ui.opcaoF.clicked.connect(self.acaoBotaoF)
        self.ui.opcaoG.clicked.connect(self.acaoBotaoG)
        self.ui.opcaoH.clicked.connect(self.acaoBotaoH)
        self.ui.opcaoI.clicked.connect(self.acaoBotaoI)
        self.ui.opcaoJ.clicked.connect(self.acaoBotaoJ)
        self.ui.opcaoK.clicked.connect(self.acaoBotaoK)
        self.ui.opcaoL.clicked.connect(self.acaoBotaoL)

        self.ui.botaoPular.clicked.connect(self.acaoPular)


    @QtCore.pyqtSlot()
    def acaoBotaoA(self):
        escolhido = 'A'
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotaoB(self):
        escolhido = 'B'
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotaoC(self):
        escolhido = 'C'
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotaoD(self):
        escolhido = 'D'
        self.verificaCorreta(escolhido)
    
    @QtCore.pyqtSlot()
    def acaoBotaoE(self):
        escolhido = 'E'
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotaoF(self):
        escolhido = "F"
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotaoG(self):
        escolhido = "G"
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotaoH(self):
        escolhido = "H"
        self.verificaCorreta(escolhido)
    
    @QtCore.pyqtSlot()
    def acaoBotaoI(self):
        escolhido = "I"
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotaoJ(self):
        escolhido = "J"
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotaoK(self):
        escolhido = "K"
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoBotaoL(self):
        escolhido = "L"
        self.verificaCorreta(escolhido)

    @QtCore.pyqtSlot()
    def acaoPular(self):
        self.m = MessageBox(self, self.dadosJson,"Recurso de Pular", "Infelizmente não é possível pular", prosseguir=False)

    def verificaCorreta(self, escolha):
        self.numCliques += 1
        self.listaDeCliques = [escolha] + self.listaDeCliques[0:4]

        print(self.listaDeCliques)

        if(self.listaDeCliques == self.opcaoCorreta):
            self.m = self.ordemJanelas.proximaTela()
            self.hide()

        if(self.numCliques > 10):
            self.ui.botaoPular.show()

    def alteraTitulo(self, titulo = ""):
        self.ui.labelTitulo.setText("Pergunta {} / 145".format(titulo))
        
class UltimaTela(QWidget):
    def __init__(self):
        super().__init__()
        self.dadosJson = DadosJSON()
        self.ui = Ui_UltimaJanela()
        self.ui.setupUi(self)
        Tentativas = self.dadosJson.getTentativas()
        Minimizadas = self.dadosJson.getMinimizadas()
        self.ui.labelMinimizadas.setText("Minimizadas: {}".format(Minimizadas))
        self.ui.labelTentativas.setText("Tentativas: {}".format(Tentativas))
        self.movie = QMovie(":/newPrefix/loader.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()
        self.ui.botaoFinalizar.clicked.connect(self.acaoFinalizar)

    @QtCore.pyqtSlot()
    def acaoFinalizar(self):
        self.close()

    
    
class MessageBox(QMessageBox,Common):

    def __init__(self, mainWindow, dadosJson, Title ="", Text="", prosseguir = False):
        self.ordemJanelas = Janelas()
        self.dadosJson = dadosJson
        super(MessageBox, self).__init__()
        mainWindow.hide()
        self.setWindowTitle(Title)
        self.setText(Text)
        self.show()
        self.posX = self.pos().x()
        self.posY = self.pos().y()
        
        self.setIcon(QtWidgets.QMessageBox.Information)

        self.configureWindow(minimizeButton=False)

        self.setStandardButtons(QtWidgets.QMessageBox.Ok)
        

        returnValue = self.exec()
        if returnValue == QMessageBox.Ok:
            if(prosseguir == True):
                self.m = self.ordemJanelas.proximaTela()
                self.hide()
            else:   
                self.close()

app = QtWidgets.QApplication(sys.argv)

ordemJanelas = Janelas()
ordemJanelas.proximaTela()

# w = UltimaTela()
# w.show()

sys.exit(app.exec_())