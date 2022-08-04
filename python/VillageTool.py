# Import necessary libraries
# from tkinter import *
# from tkinter import ttk
from rollDice import *
from ImportFiles import *

# villWin = Tk()
# villWin.title('Village Maker')

preVill = importFiles.villPre()
sufVill = importFiles.villSuf()
villShop = importFiles.villShop()

comboTown = ""

typeVill = importFiles.villType()
vType = typeVill[rollDice.d8()]

villSize = rollDice.villSize(vType)
villBiz = rollDice.villBiz(vType)

# villFrame = ttk.Frame(padding="3 3 12 12")
# villFrame.grid(column=0, row=0, sticky=(N, W, E, S))
# 
# villWin.columnconfigure(0, weight=1)
# villWin.rowconfigure(0, weight=1)
# villWin.geometry('500x300')

name1 = preVill[rollDice.d100()]
name2 = sufVill[rollDice.d50()]

# ttk.Label(villFrame, text='Choose a Village Name to Generate', justify='center').grid(column=2, row=1, sticky=(W, E))

# comboTown = StringVar(villFrame, name1 + name2)
comboTown = name1 + name2
# ttk.Label(villFrame, textvariable=comboTown).grid(column=1, row=2, sticky=(W, E))
# villWin.mainloop()

for x in range(int(villBiz)) :
    vShop = villShop[rollDice.d100()]
    vShops = 'python\contentFiles\Test.txt'

    with open(vShops, 'a') as fTest:
        fTest.write(vShop + '\n')
        fTest.close()

print('Testing Output:')
print(vType)
print(villSize)
print(villBiz)