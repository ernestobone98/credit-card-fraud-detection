from tkinter import *
from tkinter.ttk import *

master = Tk()
master.geometry('215x40')


style = Style(master)
style.configure("TRadiobutton", background = "black",
                foreground = '#d4b356', font = ("arial", 10, "bold"))
 
Radiobutton(master, text = "coucou").place(width=80, x=10, y=10)
Radiobutton(master, text ="coucou2").place(width=80, x=100, y=10)

mainloop()