from tkinter import ttk
from ttkthemes import ThemedTk

janela=ThemedTk(theme='Adapta')

def abrir():
    janela2=ThemedTk(theme='Arc')

entrada=ttk.Button(janela, text='ABRIR OUTRA JANELA', command=abrir)
entrada.grid(row=0, column=0)

janela.mainloop()