from multiprocessing import Value
import os
from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import ImageTk, Image
import subprocess as sub
from subprocess import call
from tkinter.font import Font

sep = os.path.sep

def open_message():
    with open(f"views{sep}reports{sep}message_patron.txt") as file:
        text = file.readlines()
        if len(text) != 0:
            messagebox.showinfo("Message", text)
        else:
            messagebox.showinfo("Pas de message", "Tout vas bien")

def open_report():
    call(["python3", f"controllers{sep}open_pdf.py"])

def log_out():
    window.destroy()
    sub.call(["python3", f"views{sep}login.py"])

def delete_item():
	my_list.delete(ANCHOR)

def add_item():
	my_list.insert(END, my_entry.get())
	my_entry.delete(0, END)

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
    command = open_message,
    relief = "flat",
    background= '#262A33')

b0.place(
    x = 131, y = 373,
    width = 45,
    height = 45)

canvas.create_text(
    159.0, 433.5,
    text = "Open message",
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
    text = "Open rapport",
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

###########################################################################################################################################

#################################################################################################
### -------------------------------------- TO DO LIST  -------------------------------------- ###
#################################################################################################

titre_section = tkinter.Label(text="TO DO LIST ", background="white", font=("Times New Roman", 25, 'underline'), anchor='w')
titre_section.place(height=50, width=400, x=350, y=100)

my_font = Font(family="Helvetica",	size=20)

my_frame = Frame(window).place(height=200, width=700, x=350, y=150)

my_list = Listbox(my_frame,
	font=my_font,
	width=25,
	height=5,
	bg='#dedede',
	bd=5,
	fg="black",
	highlightthickness=2,
    selectbackground="#d4b356",
    selectmod = 'browse',
	activestyle="none")

my_list.place(height=200, width=700, x=350, y=150)

my_entry = Entry(window, font=("Times New Roman", 20), width=26)
my_entry.place(height=30, width=500, x=450, y=365)

add_button = Button(text="Add Item", command=add_item, background='#d4b356').place(height=30, width=75, x=1070, y=250)
delete_button = Button(text="Delete Item", command=delete_item, background='#d4b356').place(height=30, width=75, x=1070, y=290)


###########################################################################################################################################

#################################################################################################
### ------------------------------------ PRINT CALENDAR  ------------------------------------ ### 
#################################################################################################  

from tkcalendar import Calendar

cal = Calendar(selectmode = 'day').place(height=200, width=250, x = 800, y = 460)

def grad_date():
	date.config(text = "Selected Date is: " + cal.get_date())

date = Label(text = "").place(height=200, x = 800, y = 460)
  
##################################################################################################
### ------------------------------------- TABLEAU COIN   ------------------------------------- ### 
##################################################################################################

os.environ['CRYPTOCOMPARE_API_KEY'] = '61aa8867b5734768ef4b2e53a3fc00c09cf872807ea305db867f8ff54f8fc2b8'


import cryptocompare
import threading

# Bitcoin	
# Ethereum	
# XRP
# Terra
# Dogecoin

currency_frame = Frame(window, background="white").place(height=250, width=350, x=310, y=450)

def get_crypto_price(cryptocurrency,currency):
    return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]

def get_crypto_name(cryptocurrency):
    return cryptocompare.get_coin_list()[cryptocurrency]['FullName']

def print_currencies():
    global stop
    while True:
        if stop:
            break
        # get values
        btc = get_crypto_price('BTC', 'EUR')
        eth = get_crypto_price('ETH', 'EUR')
        xrp = get_crypto_price('XRP', 'EUR')
        terra = get_crypto_price('LUNA', 'EUR')
        doge = get_crypto_price('DOGE', 'EUR')

        ### print values ###

        #btc
        btc_value = tkinter.Label(text=str(btc)+' €', background="white", font=("Times New Roman", 18), anchor='w')
        btc_value.place(height=50, width=200, x=475, y=470)

        #eth
        eth_value = tkinter.Label(text=str(eth)+' €', background="white", font=("Times New Roman", 18), anchor='w')
        eth_value.place(height=50, width=200, x=475, y=510)

        #xrp
        xrp_value = tkinter.Label(text=str(xrp)+' €', background="white", font=("Times New Roman", 18), anchor='w')
        xrp_value.place(height=50, width=200, x=475, y=550)

        #terra
        terra_value = tkinter.Label(text=str(terra)+' €', background="white", font=("Times New Roman", 18), anchor='w')
        terra_value.place(height=50, width=200, x=475, y=590)

        #doge
        dogecoin_value = tkinter.Label(text=str(doge)+' €', background="white", font=("Times New Roman", 18), anchor='w')
        dogecoin_value.place(height=50, width=200, x=475, y=630)

# BTC
btc_text = tkinter.Label(text="Bitcoin", background="white", font=("Times New Roman", 18), anchor='w')
btc_text.place(height=50, width=400, x=370, y=470)

btc = f"views{sep}img{sep}btc.png"
img_btc = PhotoImage(file = btc)
btc_label = Label(image = img_btc, background="white")
btc_label.place(x = 345, y = 485, height = 15, width = 15)

# ETH
eth_text = tkinter.Label(text="Ethereum", background="white", font=("Times New Roman", 18), anchor='w')
eth_text.place(height=50, width=400, x=370, y=510)

eth = f"views{sep}img{sep}eth.png"
img_eth = PhotoImage(file = eth)
eth_label = Label(image = img_eth, background="white")
eth_label.place(x = 345, y = 525, height = 15, width = 15)

# XRP
xrp_text = tkinter.Label(text="XRP", background="white", font=("Times New Roman", 18), anchor='w')
xrp_text.place(height=50, width=400, x=370, y=550)

xrp = f"views{sep}img{sep}xrp.png"
img_xrp = PhotoImage(file = xrp)
xrp_label = Label(image = img_xrp, background="white")
xrp_label.place(x = 345, y = 565, height = 15, width = 15)

# TERRA
terra_text = tkinter.Label(text="Terra", background="white", font=("Times New Roman", 18), anchor='w')
terra_text.place(height=50, width=400, x=370, y=590)

terra = f"views{sep}img{sep}terra.png"
img_terra = PhotoImage(file = terra)
terra_label = Label(image = img_terra, background="white")
terra_label.place(x = 345, y = 605, height = 15, width = 15)

# DOGE
dogecoin_text = tkinter.Label(text="Dogecoin", background="white", font=("Times New Roman", 18), anchor='w')
dogecoin_text.place(height=50, width=400, x=370, y=630)

doge = f"views{sep}img{sep}doge.png"
img_doge = PhotoImage(file = doge)
doge_label = Label(image = img_doge, background="white")
doge_label.place(x = 345, y = 645, height = 15, width = 15)


###################################################################################################################################
stop = False
t1 = threading.Thread(target=print_currencies, name="Tableau de valeurs")
t1.start()

window.resizable(False, False)
window.mainloop()

stop = True
t1.join()