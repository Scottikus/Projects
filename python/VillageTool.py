from rollDice import *
from ImportFiles import *

preVill = importFiles.villPre()
sufVill = importFiles.villSuf()
villShop = importFiles.villShop()
comboTown = ""

typeVill = importFiles.villType()
vType = typeVill[rollDice.d8()]

villSize = rollDice.villSize(vType)
villBiz = rollDice.villBiz(vType)


name1 = preVill[rollDice.d100()]
name2 = sufVill[rollDice.d50()]

comboTown = name1 + name2

vShops = []
for x in range(int(villBiz)):
    vShop = villShop[rollDice.d100()]
    vShops.append(vShop)


if vType == 'Thorp':
    villAge = rollDice.d3()
    doesGov = False
elif vType == 'Hamlet':
    villAge = rollDice.d4()
    doesGov = False    
elif vType == 'Village':
    villAge = rollDice.d6()
    govOrNot = rollDice.d2()
    if govOrNot == 0:
        doesGov = False
    else:
        doesGov = True
else:
    villAge = rollDice.d6()
    doesGov = True
    
print('Testing Output:')
print(vType)
print(villSize)
print(villBiz + " Businesses")
print(vShops)
print("Village Age is: "+ str(villAge))
print("Does it have a government?: " + str(doesGov))
# Import necessary libraries
# from tkinter import *
# from tkinter import ttk
# villWin = Tk()
# villWin.title('Village Maker')
# villFrame = ttk.Frame(padding="3 3 12 12")
# villFrame.grid(column=0, row=0, sticky=(N, W, E, S))
# 
# villWin.columnconfigure(0, weight=1)
# villWin.rowconfigure(0, weight=1)
# villWin.geometry('500x300')
# ttk.Label(villFrame, text='Choose a Village Name to Generate', justify='center').grid(column=2, row=1, sticky=(W, E))
# comboTown = StringVar(villFrame, name1 + name2)
# ttk.Label(villFrame, textvariable=comboTown).grid(column=1, row=2, sticky=(W, E))
# villWin.mainloop()