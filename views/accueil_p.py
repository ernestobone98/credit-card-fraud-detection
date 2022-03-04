'''
Fait par Gazzera Marco:
Interface intérieur patron
'''

'''
Les import
'''

import tkinter
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox

'''
Début du script
'''

win  = Tk()
win.title("MENU PATRON")
win.geometry("1400x700")
win.iconbitmap('img\\logo.ico')
win.configure(background='#000000')

#Pour les stats
def print_stats():
	print("Statistique")

btn_stats = Button(win, text = "Graphe", font = ("Arial", 16),bg ="#DCB253", fg = "black", command=print_stats)
btn_stats.place(x=50, y= 50, width=1300, height=550)

#Pour ouvrir le rapport
def open_report():
	file = open('rapport.txt', "r")
	line = file.readline()
	while line:
	    print(line)
	    line = file.readline()
	file.close()

btn_open_report = Button(win, text = "Rapport", font = ("Arial", 16),bg ="#DCB253", fg = "black", command=open_report)
btn_open_report.place(x=75, y= 650, width=150)

#Pour faire une decision
def decision():
	print("Decision est de")

btn_decision = Button(win, text = "Décision", font = ("Arial", 16),bg ="#DCB253", fg = "black", command=decision)
btn_decision.place(x=1175, y= 650, width=150)

'''
Fin du script
'''
win.mainloop()