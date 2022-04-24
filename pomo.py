# bibliotecas

from tkinter import *
import time

root  = Tk()
root.title("PomoDoro")  #inserir emoji/ícone e status do programa(talvez)
#root.iconbitmap('')
root.geometry('600x400')

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

def update():
    my_label.config(text = "new text")

my_label = Label(root, text="Old Text")
my_label.pack(pady=20)

my_label.after(5000, update)



root.mainloop() #quando exibir a janela, deixe-a exibida
