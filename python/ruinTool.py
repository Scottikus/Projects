# Import necessary libraries
from tkinter import *
from tkinter import ttk
import random
import os

class ruinTool():
    # Instantiate ruinWin
    ruinWin = Tk()
    ruinWin.title("Ruin Tool")

    # Arrays to pull from
    nTown = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Town_Names.txt'

    with open(nTown) as fTown:
        townName = fTown.read().splitlines()
        fTown.close()


    ruinAtt = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

    with open(ruinAtt) as fAtt:
        rStruct = fAtt.read().splitlines()[1:11]
        fAtt.close()

    with open(ruinAtt) as fAtt:
        rInhab = fAtt.read().splitlines()[13:33]
        fAtt.close()

    with open(ruinAtt) as fAtt:
        yRuin = fAtt.read().splitlines()[36:45]
        fAtt.close()

    with open(ruinAtt) as fAtt:
        longRuin = fAtt.read().splitlines()[48:56]
        fAtt.close()

    with open(ruinAtt) as fAtt:
        rCondition = fAtt.read().splitlines()[59:68]
        fAtt.close()


    # Array to store results
    rDone = ["", "", "", "", ""]

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
        if ruinTool.radChoose.get() == 1:
            name = ruinTool.town_entry.get()
        elif ruinTool.radChoose.get() == 2:
            name = ruinTool.townResult.get()
        else:
            name ="ERROR Town"

        resultFile = 'C:/Users/scott/Downloads/RuinedPlaces.txt'

        with open(resultFile, 'a') as file_object:
            file_object.write(name + " -\n" +
                              "The Ruined Structure is - " + ruinTool.rDone[0] +
                              "\nWhy was it ruined? - " + ruinTool.rDone[1] +
                              "\nCurrent Inhabitants - " + ruinTool.rDone[2] +
                              "\nHow long has it been ruined? - " + ruinTool.rDone[3] +
                              "\nRuin Condition - " + ruinTool.rDone[4] + ".\n")
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

    # Frame instantiation
    mainframe = ttk.Frame(padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    ruinWin.columnconfigure(0, weight=1)
    ruinWin.rowconfigure(0, weight=1)

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

    # Show result of random name grabbed.
    townResult = StringVar(mainframe, townName[randNum])
    ttk.Label(mainframe, textvariable=townResult).grid(column=2, row=2, sticky=(W, E))

    ttk.Radiobutton(mainframe, text="Choose this", variable=radChoose, value=1).grid(column=3, row=1, sticky=W)
    ttk.Radiobutton(mainframe, text="OR choose this", variable=radChoose, value=2).grid(column=3, row=2, sticky=W)

    town_entry.focus()
    ruinWin.bind("<Return>", generate)

    ruinWin.mainloop()
