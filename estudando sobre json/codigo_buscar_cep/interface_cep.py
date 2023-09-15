import buscador_cep as bc
import PySimpleGUI as sg
import pandas as pd

class TelaUsuario:
    def __init__(self):
        self.layout_Usuario = [
            [sg.Text('Digite seu CEP')],
            [sg.Input(key='-cep-')],
            [sg.Button('Buscar', key='Buscar')],
            [sg.Button('Fechar', key='Fechar')]
        ]
        self.janela = sg.Window('Buscador', layout=self.layout_Usuario)

    def sistema_busca(self, cep):
        cep_encontrado = bc.buscar_cep(cep)
        if cep_encontrado == 'CEP inválido':
            return 'CEP inválido'
        elif cep_encontrado == 'CEP não encontrado':
            return 'CEP não encontrado'
        else:
            return bc.filtrage(cep_encontrado)

    def run(self):
        while True:
            event, valores = self.janela.read()
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break
            elif event == 'Buscar':
                cep_digitado = valores['-cep-']
                resultado = self.sistema_busca(cep_digitado)
                if resultado == 'CEP inválido':
                    sg.popup_error('CEP inválido')
                elif resultado == 'CEP não encontrado':
                    sg.popup_error('CEP não encontrado')
                else:
                    self.mostrar_tabela(resultado)

        self.janela.close()

    def mostrar_tabela(self, resultado):
        df = pd.DataFrame([resultado], columns=['Estado', 'DDD', 'Cidade', 'Bairro', 'Rua', 'COD IBGE'])
        sg.theme('SystemDefaultForReal')
        layout = [
            [sg.Table(values=df.values.tolist(),
                       headings=df.columns.tolist(),
                       auto_size_columns=True,
                       justification='right',
                       num_rows=min(25, len(resultado)))],
            [sg.Button('Fechar')]
        ]
        window = sg.Window('Tabela de Dados', layout, finalize=True)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break

        window.close()


if __name__ == '__main__':
    tela = TelaUsuario()
    tela.run()
