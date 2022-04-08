from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os 

sep = os.path.sep

win = Tk()
win.geometry("630x700+400+100")
win.title("Open reports")
win.config(bg = "white")

def browseFiles():
	filename = filedialog.askopenfilename(initialdir = f'{os.getcwd()}{sep}views{sep}reports', 
											title = "Select a pdf file", 
											filetypes = [("PDF FILE", ".pdf")])
	
	variable1 = pdf.ShowPdf()
	#Add your pdf location and width and height.
	variable2 = variable1.pdf_view(win,pdf_location=filename,width=100,height=100)
	variable2.pack()

Button(win, text="Open", command=browseFiles, width = 40, font ="Arial 20", bd = 4).pack()

win.mainloop()
