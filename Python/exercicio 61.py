from tkinter import *
from tkinter.font import *
janela=Tk()
janela.title('progessão aritimetica')
janela.geometry('371x130+769+315')
janela.iconbitmap(default='download-_3_.ico')


a = Font(family="Lucida Grande", size=15)
msg=Label(janela, text='escreva o primeiro termo  ',  font=a )
msg.grid(row=0, column=0, sticky=W)
entr=Entry(janela, width=20)
entr.grid(row=0, column=1,)

def clique(retorno):
    print(f'x:{retorno.x} / y:{retorno.y} GEO:{janela.geometry()}')

janela.bind('<Button-3>', clique)

def pa():
    q=0
    n=entr.get()
    n = int(n)
    n1=entr2.get()
    n1 = int(n1)
    q = 0

    while q != 10:
        n = int(n)
        n1 = int(n1)

        if q == 0 :
            n = str(n)
            o = n

        elif q == 1:
            n = str(n)
            z=n

        elif q == 2 :
            n = str(n)
            y=n

        elif q == 3 :
            n = str(n)
            x=n

        elif q == 4 :
            n = str(n)
            w=n

        elif q == 5 :
            n = str(n)
            v=n

        elif q == 6 :
            n = str(n)
            u=n

        elif q == 7:
            n = str(n)
            t=n

        elif q == 8:
            n = str(n)
            s=n

        elif q == 9:
            n = str(n)
            r=n

        n = int(n)
        n = n + n1
        q = q + 1
    po= o,'-', z,'-',y,'-', x,'-', w,'-', v,'-', u,'-', t,'-', s,'-', r,'-','Fim'

    msgfi.configure(text=po)
msg2=Label(janela, text='escreva a razão',  font=a )
msg2.grid(row=1, column=0, sticky=W)
entr2=Entry(janela, width=20)
entr2.grid(row=1, column=1,)
msg0=Label(janela, text='   ',  font=a )
msg0.grid(row=2, column=0, sticky=W)
bot=Button(janela, text='obter progresão aritimética', command=pa)
bot.grid(row=3, column=0, sticky=E)

b= Font(family="Lucida Grande", size=6)
msgfi=Label(janela, text=' ', font=b)
msgfi.grid(row=4, column=0, sticky=E)








janela.mainloop()