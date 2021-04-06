# a fazer:
# Escrever operações na tela


import PySimpleGUI as sg
import math

# tamanho da tela
WIN_W = 30
WIN_H = 50

# Menu layout
menu_layout = [['File',['Exit']],
               ['Tools', ['Historic']],
               ['Help', ['About']]]

# layout
#             linha 1
layout = [[sg.Menu(menu_layout)],
          [sg.Input('0', size=(15, 1), font=('Consolas', 20), key='Box'),
          sg.Button('<-', font=('Consolas,', 20), key='Delete'),
          sg.Button('C', font=('Consolas,', 20), key='Clear')],
         [ #linha 2
             sg.Button('1', font=('Consolas,', 20), key='1'),
             sg.Button('2', font=('Consolas,', 20), key='2'),
             sg.Button('3', font=('Consolas,', 20), key='3'),
             sg.Button('+', font=('Consolas,', 20), key='+'),
             sg.Button('-', font=('Consolas,', 20), key='-'),
             sg.Button('^', font=('Consolas,', 20), key='p')],
         [ #linha 3
             sg.Button('4', font=('Consolas,', 20), key='4'),
             sg.Button('5', font=('Consolas,', 20), key='5'),
             sg.Button('6', font=('Consolas,', 20), key='6'),
             sg.Button('*', font=('Consolas,', 20), key='*'),
             sg.Button('/', font=('Consolas,', 20), key='/'),
             sg.Button('.', font=('Consolas,', 20), key='.' )],
         [ #linha 4
             sg.Button('7', font=('Consolas,', 20), key='7'),
             sg.Button('8', font=('Consolas,', 20), key='8'),
             sg.Button('9', font=('Consolas,', 20), key='9'),
             sg.Button('0', font=('Consolas,', 20), key='0'),
             sg.Button('=', font=('Consolas,', 20), key='='),
             sg.Button('√', font=('Consolas',20), key='raiz')]]

#


class TelaPython:

    def __init__(self):

        self.window = sg.Window('Calculadora', layout=layout,margins=(0 , 0), resizable=True, return_keyboard_events=False)
        self.result = 0
        self.n = 0
        self.resultado = list()
        self.momento = 0
        self.oper = ''
        self.window.read(timeout=1)
        for i in range(1, 5):
            for Button in layout[i]:
                Button.expand(expand_x=True, expand_y=True)


    def resulter(self):


        if self.values['Box'] == '':
            self.values['Box'] = int('0')

        if self.oper == '+':
            return float(self.result) + float(self.values['Box'])
        elif self.oper == '-':
            return float(self.result) - float(self.values['Box'])
        elif self.oper == '/':
            return float(self.result) / float(self.values['Box'])
        elif self.oper == '*':
            return float(self.result) * float(self.values['Box'])
        elif self.oper == 'raiz':
            num = float(self.values ['Box'])
            return float(self.result)**(1/num)
        elif self.oper == 'pow':
            return float(self.result)**float(self.values['Box'])




    def start(self):

        while True:

         #   print(self.values['Box'])

            event, self.values = self.window.read()



            if event in (None, 'Exit', sg.WIN_CLOSED): #condições para fechar o app
                break
            if event in('About'):
                sg.popup('Feito por João Rafael de Freitas Guimarães\n@joaorrafa')
            if event in ('Historic'):
               # sg.popup(f'{self.resultado}\n' * self.n)
               for i in range(0,self.n):
                   sg.easy_print(self.resultado[i])

            #funções para cada botão

            if event in('1'):
                if self.values['Box'] == '0':
                    self.window['Box'].update(value= '1')
                else:
                    self.window['Box'].update(value=self.values['Box']+'1')

            if event in ('2'):
                if self.values['Box'] == '0':
                    self.window['Box'].update(value='2')
                else:
                    self.window['Box'].update(value=self.values['Box']+'2')


            if event in('3'):
                if self.values['Box'] == '0':
                    self.window['Box'].update(value='3')
                else:
                    self.window['Box'].update(value=self.values['Box']+'3')

            if event in('4'):
                if self.values['Box'] == '0':
                    self.window['Box'].Update(value='4')
                else:
                    self.window['Box'].update(value=self.values['Box']+'4')

            if event in('5'):
                if self.values['Box'] == '0':
                    self.window['Box'].update(value='5')
                else:
                    self.window['Box'].update(value=self.values['Box']+'5')

            if event in('6'):
                if self.values['Box'] == '0':
                    self.window['Box'].update(value='6')
                else:
                    self.window['Box'].update(value=self.values['Box']+'6')

            if event in('7'):
                if self.values['Box'] == '0':
                    self.window['Box'].update(value='7')
                else:
                    self.window['Box'].update(value=self.values['Box']+'7')

            if event in('8'):

                if self.values['Box'] == '0':
                    self.window['Box'].update(value='')
                    self.window['Box'].update(value='8')
                else:
                    self.window['Box'].update(value=self.values['Box']+'8')

            if event in('9'):
                if self.values['Box'] == '0':
                    self.window['Box'].update(value='9')
                else:
                    self.window['Box'].update(value=self.values['Box']+'9')

            if event in('0'):
                if self.values['Box'] == '0':
                    self.window['Box'].update(value='0')
                else:
                    self.window['Box'].update(value=self.values['Box']+'0')
            #######
            # Operadores
            if event in ['Clear']:
                self.result = 0
                self.window['Box'].update(value=self.result)
            if event in ('Delete'):
                self.window['Box'].update(value=self.values['Box'][:-1])


            if event in ('+'):

                if self.oper != '':
                    self.result = self.resulter()
                    self.oper ='+'
                else:
                    self.oper = '+'
                    self.result = self.values['Box']

                self.window['Box'].update(value='')
            if event in ('-'):
                if self.oper != '':
                    self.result = self.resulter()
                    self.oper = '-'
                else:
                    self.oper = '-'
                    self.result = self.values['Box']
                self.window['Box'].update(value='')

            if event in ('*'):
                if self.oper != '':
                    self.result = self.resulter()
                    self.oper = '*'
                else:
                    self.oper = '*'
                    self.result = self.values['Box']

                self.window['Box'].update(value='')

            if event in ('/'):
                if self.oper != '':
                    self.result = self.resulter()
                    self.oper = '/'
                else:
                    self.oper = '/'
                    self.result = self.values['Box']
                self.window['Box'].update(value='')

            if event in ('raiz'):
                if self.oper != '':
                    self.result = self.resulter()
                    self.oper = 'raiz'
                else:
                    self.oper = 'raiz'
                    self.result = self.values['Box']
                self.window['Box'].update(value='')


                    # self.n += 1
                    # self.oper = 'raiz'
                    # self.result = self.resulter()
                    # self.resultado.append(self.result)
                    # self.window['Box'].update(value=self.result)
                    # self.oper =''

            if event in ('='):
                self.n += 1
                self.result = self.resulter()
                self.resultado.append(self.result)
                self.window['Box'].update(value=self.result)
                self.result=0
                self.oper = ''

            if event in ('pow'):
                if self.oper != '':
                    self.result = self.resulter()
                    self.oper = 'pow'
                else:
                    self.oper = 'pow'
                    self.result = self.values['Box']
                self.window['Box'].update(value='')



            #Ponto

            if event in ('.'):
                    self.window['Box'].update(value=self.values['Box'] + '.')






TelaPython().start()


# tela= TelaPython()
# tela.start()
