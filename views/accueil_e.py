from cmath import log
import os
from email.mime import image
from tkinter import *
from PIL import ImageTk, Image
from subprocess import call
import sys

sep = os.path.sep

def create_message():
    call(["python3", f"controllers{sep}write.py"])

def create_report():
    call(["python3", f"controllers{sep}pdf_generator.py"])

def log_out():
    window.destroy()
    call(["python3", f"views{sep}login.py"])

window = Tk()
window.geometry("1200x720")
window.title("Interface de l'expert")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 720,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"views{sep}img{sep}bg_inter.png")
background = canvas.create_image(
    600.0, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"views{sep}img{sep}env.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = create_message,
    relief = "flat",
    background= '#262A33')

b0.place(
    x = 131, y = 373,
    width = 45,
    height = 45)

canvas.create_text(
    159.0, 433.5,
    text = "Message(s)",
    fill = "#ffffff",
    font = ("RalewayRoman-Regular", int(18.0)))

img1 = PhotoImage(file = f"views{sep}img{sep}logout.png")

b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = log_out,
    relief = "flat",
    background='#D8BB67')

b1.place(
    x = 1149, y = 25,
    width = 25,
    height = 25)

img2 = PhotoImage(file = f"views{sep}img{sep}report.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = create_report,
    relief = "flat",
    background= '#262A33')

b2.place(
    x = 131, y = 515,
    width = 45,
    height = 45)

canvas.create_text(
    161.0, 585.5,
    text = "Génerer un rapport",
    fill = "#ffffff",
    font = ("RalewayRoman-Regular", int(18.0)))

if sys.argv[1] == 'be816425':
    img3 = PhotoImage(file = f"views{sep}img{sep}ernesto.png")
    name = 'Ernesto'
elif sys.argv[1] == 'gm801217':
    img3 = PhotoImage(file = f"views{sep}img{sep}marco.png")
    name = 'Marco'

b3 = Label(
    background='#262A33',
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b3.place(
    x = 110, y = 135,
    width = 88,
    height = 88)

canvas.create_text(
    159.0, 260.5,
    text = name,
    fill = "#ffffff",
    font = ("RalewayRoman-Regular", int(18.0)))

window.resizable(False, False)
window.mainloop()