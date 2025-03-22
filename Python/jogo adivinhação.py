from tkinter import *
from random import randint
n=0
janela = Tk()
janela.title('jogo da adivinhação 2.2.0')
janela.geometry('300x500+459+45')
janela.resizable(False, False)


imgp= PhotoImage(file='jogo da adivinhação.png')
labelpng=Label(janela, image=imgp)
labelpng.pack()
labelpng.place(x=0, y=0)


def clique(retorno):
    print(f'x:{retorno.x} / y : {retorno.y} geo :{janela.geometry()}')
janela.bind('<Button-3>', clique)

#comandos
numa = 0

def co1():
    numa = randint(1, 5)
    n=1
    if n == numa:
        ent.configure(text='parabens, acertou! ')
    else:
        ent.configure(text=numa)
def co2():
    numa = randint(1, 5)
    n=2
    if n == numa:
        ent.configure(text='parabens, acertou !')
    else:
        ent.configure(text=numa)
def co3():
    numa = randint(1, 5)
    n=3
    if n == numa:
        ent.configure(text='parabens, acertou !')
    else:
        ent.configure(text=numa)
def co4():
    numa = randint(1, 5)
    n=4
    if n == numa:
        ent.configure(text='parabens, acertou!')
    else:
        ent.configure(text=numa)
def co5():
    numa = randint(1, 5)
    n=5
    if n == numa:
        ent.configure(text='parabens, acertou !')
    else:
        ent.configure(text=numa)
#criacao de botoes:

bot1=Button(janela, text='1', font='Abscissa 60', borderwidth=1, command=co1)
bot1.place(x=16, y=238, width=87, height=87)

bot2=Button(janela, text='2', font='Abscissa 60', borderwidth=1, command=co2)
bot2.place(x=111, y=238, width=87, height=87)

bot3=Button(janela, text='3', font='Abscissa 60', borderwidth=1, command=co3)
bot3.place(x=205, y=238, width=87, height=87)

bot4=Button(janela, text='4', font='Abscissa 60', borderwidth=1, command=co4)
bot4.place(x=57, y=336, width=87, height=87)

bot5=Button(janela, text='5',font='Abscissa 60', borderwidth=1, command=co5)
bot5.place(x=164, y=336, width=87, height=87)

#entada de computador

ent=Label(janela, font='Arial 10', text='',)
ent.place(x=142, y= 463, width=120, height=20)






janela.mainloop()
