# bibliotecas

from tkinter import *
import time

root  = Tk()
root.title("PomoDoro")  #inserir emoji/ícone e status do programa(talvez)
#root.iconbitmap('')
root.geometry('600x400')
root.configure(bg='#fc5549')

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    my_label.config(text = hour + ":" + minute + ":" +second)
    my_label.after(1000, clock)

def update():
    my_label.config(text="New Text")


my_label = Label(root, text="", font=("Helvetica",  48), fg = 'white', bg= '#ff675c' )
my_label.pack(pady=20)

my_label2 = Label(root, text="")



clock()

#my_label.after(5000, update)



root.mainloop() #quando exibir a janela, deixe-a exibida
