# Import necessary libraries
from tkinter import *
from tkinter import ttk
from operator import concat
import random

villWin = Tk()
villWin.title('Village Maker')

villPre = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Village_Prefixes.txt'

with open(villPre) as fPre:
    preVill = fPre.read().splitlines()
    fPre.close()

villSuf = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Village_Suffixes.txt'

with open(villSuf) as fSuf:
    sufVill = fSuf.read().splitlines()
    fSuf.close()

comboTown = ""

# Rolling the Dice
def rollDice(dice: str):
    if dice == 'd20':
        r = random.randint(0, 19)
        return r
    elif dice == 'd12':
        r = random.randint(0, 11)
        return r
    elif dice == 'd10':
        r = random.randint(0, 9)
        return r
    elif dice == 'd8':
        r = random.randint(0, 7)
        return r
    elif dice == 'd6':
        r = random.randint(0, 5)
        return r
    elif dice == 'd4':
        r = random.randint(0, 3)
        return r
    elif dice == 'd100':
        r = random.randint(0, 99)
        return r
    else:
        return 'ERROR! The input you have chosen was invalid.'

villFrame = ttk.Frame(padding="3 3 12 12")
villFrame.grid(column=0, row=0, sticky=(N, W, E, S))
villWin.columnconfigure(0, weight=1)
villWin.rowconfigure(0, weight=1)
villWin.geometry('300x500')

randNum1 = random.randint(0, 49)

name1 = preVill[rollDice('d100')]
name2 = sufVill[randNum1]

ttk.Label(villFrame, text='Choose a Village Name to Generate', justify='center').grid(column=2, row=1, sticky=(W, E))

comboTown = StringVar(villFrame, name1 + name2)
ttk.Label(villFrame, textvariable=comboTown).grid(column=1, row=2, sticky=(W, E))

villWin.mainloop()