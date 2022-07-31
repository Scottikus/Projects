# Import necessary libraries
from tkinter import *
from tkinter import ttk
import random
import os

# Instantiate Window
window = Tk()
window.title("DnD Tool")

# Arrays to pull from
nTown= 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Town_Names.txt'

with open(nTown) as fTown:
    townName = fTown.read().splitlines()


ruinAtt = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

with open(ruinAtt) as fAtt:
    rStruct = fAtt.read().splitlines()[1:11]

with open(ruinAtt) as fAtt:
    rInhab = fAtt.read().splitlines()[13:33]

with open(ruinAtt) as fAtt:
    yRuin = fAtt.read().splitlines()[36:45]

with open(ruinAtt) as fAtt:
    longRuin = fAtt.read().splitlines()[48:56]

with open(ruinAtt) as fAtt:
    rCondition = fAtt.read().splitlines()[59:68]

villPre = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Village_Prefixes.txt'

with open(villPre) as fPre:
    preVill = fPre.read().splitlines()

villSuf = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Village_Suffixes.txt'

with open(villSuf) as fSuf:
    sufVill = fSuf.read().splitlines()


# Array to store results
rDone = ["", "", "", "", ""]

pre1 = ""
suf1 = ""

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
    elif dice == '50':
        r = random.randint(0, 49)
    else:
        return 'ERROR! The input you have chosen was invalid.'

# Put results in txt file.
def generate():
    if radChoose.get() == 1:
        name = town_entry.get()
    elif radChoose.get() == 2:
        name = townResult.get()
    else:
        name ="ERROR Town"
    
    resultFile = 'C:/Users/scott/Downloads/RuinedPlaces.txt'

    with open(resultFile, 'a') as file_object:
        file_object.write(name + " -\n" +
                          "The Ruined Structure is - " + rDone[0] +
                          "\nWhy was it ruined? - " + rDone[1] +
                          "\nCurrent Inhabitants - " + rDone[2] +
                          "\nHow long has it been ruined? - " + rDone[3] +
                          "\nRuin Condition - " + rDone[4] + ".\n")
        file_object.write('\n')

    print('Ruin has been saved to the RuinedPlaces file!')
    osCommandString = "notepad.exe C:/Users/scott/Downloads/RuinedPlaces.txt"
    os.system(osCommandString)

# Random Number for getting town name.
randNum = random.randint(0, 306)
randNum50 = random.randint(0, 49)

# store results in the rDone array
rDone[0] = rStruct[rollDice("d10")]
rDone[1] = yRuin[rollDice("d10")]
rDone[2] = rInhab[rollDice("d20")]
rDone[3] = longRuin[rollDice("d8")]
rDone[4] = rCondition[rollDice("d10")]
pre1 = preVill[rollDice('d100')]
suf1 = sufVill[randNum50]

# Frame instantiation
mainframe = ttk.Frame(padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# initialize variable for radio button
radChoose = IntVar()
radChoose.set(1)

# initialize entry for custom name
nameTown = StringVar()
town_entry = ttk.Entry(mainframe, width=20, textvariable=nameTown)
town_entry.grid(column=2, row=1, sticky=(W, E))

# Put in buttons and labels
ttk.Button(mainframe, text="Generate!", command=generate).grid(column=3, row=7, sticky=W)
ttk.Label(mainframe, text="Random Town:", justify='right').grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Ruin Name:", justify='right').grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Combination Town:", justify='right').grid(column=1, row=3, sticky=W)

# Show result of random name grabbed.
townResult = StringVar(mainframe, townName[randNum])
ttk.Label(mainframe, textvariable=townResult).grid(column=2, row=2, sticky=(W, E))

comboTown = StringVar(mainframe, pre1 + suf1)
ttk.Label(mainframe, textvariable=comboTown).grid(column=2, row=3, sticky=(W, E))

ttk.Radiobutton(mainframe, text="Choose this", variable=radChoose, value=1).grid(column=3, row=1, sticky=W)
ttk.Radiobutton(mainframe, text="OR choose this", variable=radChoose, value=2).grid(column=3, row=2, sticky=W)
ttk.Radiobutton(mainframe, text="OR choose this", variable=radChoose, value=3).grid(column=3, row=3, sticky=W)

town_entry.focus()
window.bind("<Return>", generate)

window.mainloop()
