import PySimpleGUI as sg

# tamanho da tela
WIN_W = 30
WIN_H = 50

# Menu layout
menu_layout = [['File', ['Save', 'Exit']],
               ['Tools', ['Wainting']],
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
             sg.Button('-', font=('Consolas,', 20), key='-')],
         [ #linha 3
             sg.Button('4', font=('Consolas,', 20), key='4'),
             sg.Button('5', font=('Consolas,', 20), key='5'),
             sg.Button('6', font=('Consolas,', 20), key='6'),
             sg.Button('*', font=('Consolas,', 20), key='*'),
             sg.Button('/', font=('Consolas,', 20), key='/')],
         [ #linha 4
             sg.Button('7', font=('Consolas,', 20), key='7'),
             sg.Button('8', font=('Consolas,', 20), key='8'),
             sg.Button('9', font=('Consolas,', 20), key='9'),
             sg.Button('0', font=('Consolas,', 20), key='0'),
             sg.Button('=', font=('Consolas,', 20), key='=')]]

#


class TelaPython:

    def __init__(self):

        self.window = sg.Window('Calculadora', layout=layout,margins=(0 , 0), resizable=True, return_keyboard_events=False)
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1)
        for i in range(1, 5):
            for Button in layout[i]:
                Button.expand(expand_x=True, expand_y=True)


    def Result(self):

        if self.oper == '+':
            return float(self.result) + float(self.values['Box'])
        if self.oper == '-':
            return float(self.result) - float(self.values['Box'])
        if self.oper == '/':
            return float(self.result) / float(self.values['Box'])
        if self.oper == '*':
            return float(self.result) * float(self.values['Box'])



    def start(self):

        while True:
            event, self.values = self.window.read()

            if event in (None, 'Exit', sg.WIN_CLOSED): #condições para fechar o app
                break

            #funções para cada botão

            if event in('1'):
                if self.values['Box'] == 0:
                    self.window['Box'].Uptade(value='1')
                else:
                    self.window['Box'].Uptade(value=self.values['Box']+'1')

            if event in ('2'):
                if self.values['Box'] == 0:
                    self.window['Box'].Uptade(value='2')
                else:
                    self.window['Box'].Uptade(value=self.values['Box']+'2')

            if event in('3'):
                if self.values['Box'] == 0:
                    self.window['Box'].Uptade(value='3')
                else:
                    self.window['Box'].Uptade(value=self.values['Box']+'3')

            if event in('4'):
                if self.values['Box'] == 0:
                    self.window['Box'].Update(value='4')
                else:
                    self.window['Box'].Uptade(value=self.values['Box']+'4')

            if event in('5'):
                if self.values['Box'] == 0:
                    self.window['Box'].Uptade(value='5')
                else:
                    self.window['Box'].Uptade(value=self.values['Box']+'5')

            if event in('6'):
                if self.values['Box'] == 0:
                    self.window['Box'].Uptade(value='6')
                else:
                    self.window['Box'].Uptade(value=self.values['Box']+'6')

            if event in('7'):
                if self.values['Box'] == 0:
                    self.window['Box'].UptInade(value='7')
                else:
                    self.window['Box'].Uptade(value=self.values['Box']+'7')

            if event in('8'):
                if self.values['Box'] == 0:
                    self.window['Box'].Uptade(value='8')
                else:
                    self.window['Box'].Uptade(value=self.values['Box']+'8')

            if event in('9'):
                if self.values['Box'] == 0:
                    self.window['Box'].Uptade(value='9')
                else:
                    self.window['Box'].Uptade(value=self.values['Box']+'9')

            if event in('0'):
                if self.values['Box'] == 0:
                    self.window['Box'].Uptade(value='0')
                else:
                    self.window['Box'].Uptade(value=self.values['Box']+'0')
            #######

            if event in ['Clear']:
                self.result= 0
                self.window['Box'].update(value=self.result)
            if event in ('Delete'):
                self.window['Box'].update(value=self.values['Box'][:-1])


            if event in ('+'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '+'
                    self.result = self.values['Box']
                self.window['Box'].uptade(value='')

            if event in ('-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '+'
                    self.result = self.values['Box']
                self.window['Box'].uptade(value='')

            if event in ('*'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '+'
                    self.result = self.values['Box']
                self.window['Box'].uptade(value='')

            if event in ('/'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '+'
                    self.result = self.values['Box']
                self.window['Box'].uptade(value='')

            if event in ('='):
                self.result = self.resulter()
                self.window['Box'].update(value=self.result)
                self.result=0
                self.oper = ''


TelaPython().start()


# tela= TelaPython()
# tela.start()
