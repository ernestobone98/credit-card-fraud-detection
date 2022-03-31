from tkinter import ttk, Tk
from tkinter import *
import os

sep = os.path.sep

win  = Tk()
win.title("CONNEXION CLIENT")
win.geometry("300x575")
win.resizable(False, False)
win.configure(background= '#F0F0F0')

def arte():
    print("Rien a signialer tout vas bien !")

img = PhotoImage(file = f"views{sep}img{sep}iphone.png")
lbl_picture = Label (win, image=img)
lbl_picture.place(x = -42, y = -10)

btn_information = Button(win, text ="ALERTE", command = arte, padx = 40, pady = 5, background = "black", foreground = "red")
btn_information.place(x=120, y=150)

img0 = PhotoImage(file = f"views{sep}img{sep}alerte.png")
lbl_picture_alert = Label (win, image=img0)
lbl_picture_alert.place(x=40, y=135)

img1 = PhotoImage(file = f"views{sep}img{sep}bd.png")
lbl_picture_logo = Label (win, image=img1)
lbl_picture_logo.place(x=200, y=55)

img2 = PhotoImage(file = f"views{sep}img{sep}image_centre.png")
lbl_picture_centre = Label (win, image=img2)
lbl_picture_centre.place(x=40, y=200)

img1_2 = PhotoImage(file = f"views{sep}img{sep}bd_2.png")
lbl_picture_logo_2 = Label (win, image=img1_2)
lbl_picture_logo_2.place(x=152, y=225)
win.mainloop()