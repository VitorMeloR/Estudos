import pyautogui as pg
import PySimpleGUI as ps

class tela():
    def __init__(self):
        self.layout = [[ps.Button('Iniciar estudos')], [ps.Button('Terminar estudos')]]
        self.janela = ps.Window('Vamos estudar', layout=self.layout)

    def run(self):
        event = self.janela.read()
        if event == 'iniciar estudos':
            pass

class estudos():
    def __init__(self):
        self.

    def nova_area(self):

tela = tela()
tela.run()