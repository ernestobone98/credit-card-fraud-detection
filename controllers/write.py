from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
import os

sep = os.path.sep

def export():
    with open(f"views{sep}reports{sep}message_client.txt", 'w') as f:
        f.write(textbox.get("1.0", END).strip())

win = Tk()
win.title("Ecrire votre message")
textbox = ScrolledText(win)
textbox.pack(fill=BOTH, expand=YES)
Button(win, text="Export", command=export).pack(fill=X)
win.mainloop()
