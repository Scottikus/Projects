# Import necessary libraries
# from tkinter import *
# from tkinter import ttk
import random
# import os
from .rollDice import *
from .ImportFiles import *

# Instantiate Window
# window = Tk()
# window.title("Ruin Tool")

# Arrays to pull from
townName = importFiles.townName()
rStruct = importFiles.rStruct()
yRuin = importFiles.yRuin()
rInhab = importFiles.rInhab()
longRuin = importFiles.longRuin()
rCondition = importFiles.rCondition()

# Array to store results
rDone = ["", "", "", "", ""]

# Put results in txt file.
#def generate():
#    if radChoose.get() == 1:
#        name = town_entry.get()
#    elif radChoose.get() == 2:
#        name = townResult.get()
#    else:
#        name ="ERROR Town"
#    
#    resultFile = 'worldBuildSite/ruinGen/utils/contentFiles/RuinedPlaces.txt'
#
#    with open(resultFile, 'a') as f:
#        f.write(name + " -\n" +
#                "The Ruined Structure is - " + rDone[0] +
#                "\nWhy was it ruined? - " + rDone[1] +
#                "\nCurrent Inhabitants - " + rDone[2] +
#                "\nHow long has it been ruined? - " + rDone[3] +
#                "\nRuin Condition - " + rDone[4] + ".\n")
#        f.write("\n")
#
#    print('Ruin has been saved to the RuinedPlaces file!')
#    osCommandString = "notepad.exe worldBuildSite/ruinGen/utils/contentFiles/RuinedPlaces.txt"
#    os.system(osCommandString)

# Put results in txt file.
def generate2():
    results = ["", "", "", "", "", ""]
    results[0] = townResult.get()

    results[1] = rDone[0]
    results[2] = rDone[1]
    results[3] = rDone[2]
    results[4] = rDone[3]
    results[5] = rDone[4]

    # print('Ruin has been saved to the RuinedPlaces file!')
    # osCommandString = "notepad.exe python/contentFiles/RuinedPlaces.txt"
    # os.system(osCommandString)
    return results

# Random Number for getting town name.
randNum = random.randint(0, 306)

# store results in the rDone array
rDone[0] = rStruct[rollDice.d10()]
rDone[1] = yRuin[rollDice.d10()]
rDone[2] = rInhab[rollDice.d20()]
rDone[3] = longRuin[rollDice.d8()]
rDone[4] = rCondition[rollDice.d10()]

# Frame instantiation
#mainframe = ttk.Frame(padding="3 3 12 12")
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#window.columnconfigure(0, weight=1)
#window.rowconfigure(0, weight=1)
#
## initialize variable for radio button
#radChoose = IntVar()
#radChoose.set(1)
#
## initialize entry for custom name
#nameTown = StringVar()
#town_entry = ttk.Entry(mainframe, width=20, textvariable=nameTown)
#town_entry.grid(column=2, row=1, sticky=(W, E))
#
## Put in buttons and labels
#ttk.Button(mainframe, text="Generate!", command=generate).grid(column=3, row=7, sticky=W)
#ttk.Label(mainframe, text="Random Town:", justify='right').grid(column=1, row=2, sticky=W)
#ttk.Label(mainframe, text="Ruin Name:", justify='right').grid(column=1, row=1, sticky=W)
#
## Show result of random name grabbed.
#townResult = StringVar(mainframe, townName[randNum])
#ttk.Label(mainframe, textvariable=townResult).grid(column=2, row=2, sticky=(W, E))
#
#ttk.Radiobutton(mainframe, text="Choose this", variable=radChoose, value=1).grid(column=3, row=1, sticky=W)
#ttk.Radiobutton(mainframe, text="OR choose this", variable=radChoose, value=2).grid(column=3, row=2, sticky=W)
#
#town_entry.focus()
#window.bind("<Return>", generate)
#
#window.mainloop()
