from tkinter import *
import os

sep = os.path.sep
cur_dir = os.getcwd()

Fenetre = Tk()
#Bon définit le déplcement de notre objet
def deplacement():
    img_coords = canvas.coords (image)
    img_width = img_2.width()
    if img_coords [0] + img_width <= 880:
        canvas.move(image, 5, 0)
        Fenetre.after(40, deplacement)
                    

img = PhotoImage(file = f"views{sep}img{sep}dollar.gif")
#otre Canevas
canvas = Canvas (Fenetre, width=800, height=800, bg="white")
canvas.pack(padx=18,pady=10)

img_2 = img.subsample(2,2)

image = canvas.create_image(10,10, anchor = NW, image = img_2)

deplacement ()
Fenetre.mainloop()