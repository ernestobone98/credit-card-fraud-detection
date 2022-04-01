from cmath import log
import os
from email.mime import image
from tkinter import *
from PIL import ImageTk, Image
import subprocess as sub
from subprocess import call

sep = os.path.sep

def create_message():
    call(["python3", f"controllers{sep}write.py"])

def open_report():
    cmd = ['ls', f'views{sep}reports{sep}']
    report_name = sub.check_output(cmd).decode('utf-8').split('\n')[-2]
    rapport = f"views{sep}reports{sep}{report_name}"  # on doit changer et faire attention car le nom change donc voir pour le nom des rapports
    os.system(f'xdg-open {rapport}')

def log_out():
    window.destroy()
    sub.call(["python3", f"views{sep}login.py"])

window = Tk()
window.geometry("1200x720")
window.title("Interface du patron")
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

rep = f"views{sep}img{sep}report.png"
img2 = PhotoImage(file = rep)
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = open_report,
    relief = "flat",
    background= '#262A33')

b2.place(
    x = 131, y = 515,
    width = 45,
    height = 45)

canvas.create_text(
    161.0, 585.5,
    text = "Ouvrir un rapport",
    fill = "#ffffff",
    font = ("RalewayRoman-Regular", int(18.0)))

img3 = ImageTk.PhotoImage(Image.open(f"views{sep}img{sep}benjamin.png"))
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
    169.0, 260.5,
    text = "Benjamin",
    fill = "#ffffff",
    font = ("RalewayRoman-Regular", int(18.0)))

window.resizable(False, False)
window.mainloop()