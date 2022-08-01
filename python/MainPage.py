# Import necessary libraries
from tkinter import *
from tkinter import ttk

# Instantiate Window
window = Tk()
window.title("DnD Tool")

def RuinTool():
    mainframe.destroy()

    secondframe = ttk.Frame(padding="3 3 12 12")
    secondframe.grid(column=0, row=0, sticky=(N, W, E, S))
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

mainframe = ttk.Frame(padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)


ttk.Label(mainframe, text="Welcome to my DnD Flavor Generator").grid(column=1, row=1)

ttk.Button(mainframe, text="Ruin Tool", command=RuinTool).grid(column=2, row=3, sticky=(W, E))

window.mainloop()