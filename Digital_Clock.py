from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.resizable(False, False)

def time():
    string = strftime('%H:%M:%S %p\n %d-%m-%Y ')
    label.config(text = string)
    label.after(1000,time)

label = Label(root , font=("Arial",35) , background = "black" , foreground="cyan")
label.pack(anchor="center")
time()

mainloop()


# Made By Yasin Rezvani
