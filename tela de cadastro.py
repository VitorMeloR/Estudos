import base_dados
import matriz_sod
import PySimpleGUI as sg

class Tela:
    def __init__(self):
        self.error_cpf = False
        self.error_login = False
        self.error_senha = False
        self.layout = [
            [sg.Text('LOGIN '), sg.Input(key='-LOGIN-')],
            [sg.Text('SENHA'), sg.Input(key='-SENHA-')],
            [sg.Text('CPF    '), sg.Input(key='-CPF-')],
            [sg.Button('Enviar dados')],
            [sg.Button('Sair')]
        ]
        self.janela = sg.Window('Tela de cadastro', layout=self.layout)

    def sistema_login(self, login_digitado):
        verificar_login = base_dados.login(login_digitado)
        if not verificar_login:
            sg.popup_error('LOGIN DEVE CONTER 5 A 15 CARACTERES')
            self.error_login = False
        else:
            self.error_login = True
            return verificar_login

    def sistema_senha(self,senha_digitada):
        verificar_senha = base_dados.senha(senha_digitada)
        if not verificar_senha:
            sg.popup_error('A senha deve conter pelo menos 1 caractere especial, 1 número e 1 letra maiúscula.')
            self.error_senha = False
        elif verificar_senha == 8:
            sg.popup_error('A senha deve conter 8 digitos')
            self.error_senha = False
        else:
            self.error_senha = True
            return verificar_senha

    def sistema_cpf(self, cpf_digitado):
        verificar_cpf = base_dados.cpf(cpf_digitado)
        if not verificar_cpf:
            sg.popup_error('CPF INVÁLIDO')
            self.error_cpf = False
        else:
            self.error_cpf = True
            return verificar_cpf
    def run(self):
        while True:
            event, values = self.janela.read()
            if event == 'Sair' or event == sg.WIN_CLOSED:
                break
            elif event == 'Enviar dados':
                login_digitado = values['-LOGIN-']
                senha_digitada = values['-SENHA-']
                cpf_digitado = values['-CPF-']

                if self.sistema_login(login_digitado) and self.sistema_senha(senha_digitada) and self.sistema_cpf(cpf_digitado):
                    analise = base_dados.cadastrar_dados(login_digitado,senha_digitada,cpf_digitado)
                    if not analise:
                        sg.popup_error('Dados já cadastrados no sistema')
                    else:
                        sg.popup('Dados cadastrados com sucesso')
                else:
                    if not self.error_login:
                        self.janela['-LOGIN-'].update('')
                    if not self.error_senha:
                        self.janela['-SENHA-'].update('')
                    if not self.error_cpf:
                        self.janela['-CPF-'].update('')

        self.janela.close()
        sg.popup('Sistema encerrado')

tela = Tela()
tela.run()
