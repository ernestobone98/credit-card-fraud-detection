from tkinter import ttk, Tk
from tkinter import *
import os

sep = os.path.sep

win  = Tk()
win.title("CONNEXION CLIENT")
win.geometry("300x575")
win.resizable(False, False)
win.configure(background= '#D9D9D9')


def deplacement():
    img_coords = canvas.coords (image)
    img_width = img_dollar_2.width()
    if img_coords [0] + img_width <= 880:
        canvas.move(image, 1, 0)
        win.after(70, deplacement)
                    
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


img_dollar = PhotoImage(file = f"views{sep}img{sep}dollar.gif")

canvas = Canvas (win, width=160, height=40, bg='#D9D9D9')
canvas.place(x=30,y=63)

img_dollar_2 = img_dollar.subsample(2,2)

image = canvas.create_image(0,0, anchor = NW, image = img_dollar_2)

deplacement ()

win.mainloop()