from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
import os

sep = os.path.sep

def export():
    with open(f"views{sep}reports{sep}message_patron.txt", 'w') as f:
        f.write(textbox.get("1.0", END).strip())
def close():
    win.destroy()
    
win = Tk()
win.title("Write your message for the boss")
textbox = ScrolledText(win)
textbox.pack(fill=BOTH, expand=YES)
Button(win, text="Send", command=lambda:[export(),close()]).pack(fill=X)

win.mainloop()
