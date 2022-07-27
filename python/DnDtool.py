# Import necessary libraries
from tkinter import *
from tkinter import ttk
import random
import os

# Instantiate Window
window = Tk()
window.title("DnD Tool")

# Arrays to pull from
townName = [
    "Copstage", "Bowthorpe", "Oweninny", "Wickerton", "Bridgnorth", "Mamble", "Lakedon", "Castley", "Rainhill",
    "Innswood", "Eriskay", "Wychavon", "Goodminton", "Spen", "Cumnock", "Bridgefalls", "Midgham", "Stow",
    "Northwick", "Upwaltham", "Chatwell", "Eagletree", "Ewyas Harold", "Farthinghoe", "Getty's Peak", "Ystumllwynarth",
    "Milston",
    "Inkdon", "Winson", "Little Bridge", "Knightsroost", "Patrington", "Tandragee", "Crestbourne", "Pitney",
    "Uppington",
    "Summerton", "Lenham", "Bunowen", "Hawksmoor", "Beeford", "Orcheston", "Mintwillow", "Skendleby", "Ashcott",
    "Helenton", "Freckenham", "Purton", "Hillcrest", "Bardney", "Springthorpe", "Ropewalker", "Grindon", "Troutbeck",
    "Presthorpe", "Ballygub", "Skinningrove", "Fiddlegreen", "Palace", "Ounageeragh", "Ryefield", "Ullauns",
    "Uplowman",
    "Barnsey", "Wimpstone", "Ecclesfield", "Dogsbody", "Pollokshields", "Faxfleet", "Cornhenge", "Hinstock",
    "Allerthorpe",
    "Ashbourne", "Portpatrick", "Notton", "Hutton", "Penarlâg", "Bloxholm", "Beaksdale", "Ballyconneely", "Tandridge",
    "Butterpond", "Orgreave", "Drumbrughas", "Starling", "Sporle", "Elmley", "Meadhaven", "Tetchill", "Tay",
    "Darlajex", "Hedley on the Hill", "Lyrenagreena", "Swallowbeak", "Portloman", "Worlingworth", "Boarsrest",
    "Shrough", "Alvechurch",
    "Kriggan", "Appledore", "Wiggenhall", "Dundertun", "Crewe", "Ashdown Forest", "Goldcrest", "Saint Bees", "Munsley",
    "Sweetmount", "Blatchington", "Curraghlawn", "Vintnerdale", "Siefton", "Ballycrossaun", "Elkhorn", "Farthinghoe",
    "Offley",
    "Arsington", "Gortnahoe", "Tickenham", "Pottersfield", "Chilwell", "Wolsingham", "Merryhall", "Harlow Hill",
    "Lettermullan",
    "Timbersprout", "Astley", "Clent", "Gracey Peaks", "Berrow Green", "Corrandulla", "Winter's End", "Attenborough",
    "Pickworth",
    "Donaville", "Glanaman", "Leek Wootton", "Hevensbreath", "Dalwhinnie", "Blackwood", "Blythewood", "Elvetham",
    "Ousefleet",
    "Goldpeak", "Ballyboghal", "Barham", "Heathenschurch", "Hilborough", "Ballinameen", "Fleet Landing",
    "Chiddingstone", "Sollom",
    "Windrest", "Tain", "Curragh", "Windybrook", "Wartnaby", "Lifford", "Bowen's Island", "Ewell",
    "Illston on the Hill",
    "Kingsford", "Shrigley Pott", "Braunton", "Snowygap", "Peterborough", "Rainow", "Tugby", "Harvenset", "Codrington",
    "Clericsfold", "Musbury", "Wesham", "Rainvalley", "Alexandria", "Grianan", "Crudgington", "Wishleaf", "Brotherton",
    "Nettlebed", "Grendale", "Branxton", "Curdridge", "Plodburg", "Morvah",
    "Clontoe", "Felderford", "Babbacombe", "Warninglid", "Twindleton", "Ballyheelan",
    "Whiteparish", "Stagcross", "Killarney", "Lissycasey", "Hollybranch", "Treforys",
    "Ballycommon", "Threader's Hollow", "Pyecombe", "Althorp", "Silverton", "Hawick",
    "Ilton", "Ashpoint", "Snaefell", "Ashwell", "Dalmhurst", "Weybread",
    "Headlam", "Ravenwood", "Fife", "Woodchurch", "Smackover", "Kesgrave",
    "Budbrooke", "Starrynight", "Avonmouth", "Bardsey Island", "Underthal", "Ashmansworth",
    "Chell Heath", "Saint Michaelsheights", "Marlborough", "Palgrave", "Little Peachingston", "Casnewydd-ar-Wysg",
    "Ilminster", "Featherfall", "Aller", "Messing", "Cripple Creek", "Braemar",
    "Swanley", "Featherfoot", "Willand", "Bierton", "Riddle Reach", "Bredfield",
    "Crow", "Wundwin", "Dewlish", "Cliftonville", "Guildingston", "Tibthorpe",
    "Canonbury", "Maubid", "Ballymartin", "Uisge-Labhair", "Jebend", "Ardsheelane",
    "Wroxham", "San Serif", "Rodbourne", "Rath", "Shorley-Knott", "Aberavon", "Supbrough",
    "Mancot Royal", "Orcsnout", "Casnewydd Green", "Benwick", "Aeby-on-Sea", "Peckleton", "Tiltonsville",
    "Ballycrissane", "Sevenclaw", "Woodstock", "Cowlinge", "Smolton", "Penistone", "Glen Robins",
    "Theydon Bois", "Crag", "Totternhoe", "Blockley", "Hunose-Weir", "Wakerley", "Mount Pleasant",
    "Alwalton", "Wishbone", "Tindale", "Brafferton", "Fockery", "Soulby", "Martin's Ferry",
    "Petersham", "Wagonrut", "West", "Hammersmith", "Neistermeechia", "Tilford", "Deep Run",
    "Penrhyn-Llŷn", "Endtown", "Crux Easton", "Wallasey", "Shavebury", "Veryan", "Elm Grove",
    "Catfield", "Mangle", "Mere", "Cowling", "Downloe", "Shadyside"
]

rStruct = [
    "A small collection of huts"
    , "A grand noble’s manor"
    , "A temple or monastery"
    , "A mighty citadel"
    , "A single cottage"
    , "A once mighty wizard’s tower"
    , "A cemetery or tomb"
    , "A small hamlet"
    , "A town or village"
    , "A city or major settlement"
]

rInhab = [
    "Groups of bandits or criminals"
    , "Swarms of vermin"
    , "Social outcasts looking for a new home"
    , "Haunted by ghosts or spirits"
    , "Swarms of insects"
    , "Savage beasts"
    , "Refugees with nowhere else to go"
    , "Hordes of undead"
    , "Rebels acting against the local ruler"
    , "Brand new settlers"
    , "A group of traders collecting resources"
    , "Religious fanatics or cult members"
    , "Groups of giants"
    , "Eldritch beings"
    , "A mighty and cunning dragon"
    , "Survivors of the ruin’s original purpose"
    , "Plant creatures"
    , "Friendly adventuring group passing through"
    , "A wizard that is up to no good"
    , "No one; it is truly abandoned"
]
yRuin = [
    "Disease / Plague"
    , "Economic or Political Collapse"
    , "Monster Invasion"
    , "Evil Curse"
    , "Overgrowth"
    , "Victims of a Great War"
    , "A Natural Disaster"
    , "Infestation"
    , "Wrath of an Angry God"
    , "A Magical Catastrophe"
]
longRuin = [
    "Before Recorded History"
    , "1d6 Centuries Ago"
    , "1d6 Decades Ago"
    , "1d6 Years Ago"
    , "1d6 Months Ago"
    , "1d6 Weeks Ago"
    , "1d6 Days Ago"
    , "1d6 Hours Ago"
]
rCondition = [
    "Crumbling / Decayed"
    , "Disfigured / Desecrated"
    , "Infested"
    , "Corroded / Eroded"
    , "Collapsed and Broken"
    , "Crystallized / Petrified In Stone"
    , "Contaminated"
    , "Overgrown / Fungal"
    , "Still Partially Operational"
    , "Fully Operational"
]

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

# store results in the rDone array
rDone[0] = rStruct[rollDice("d10")]
rDone[1] = yRuin[rollDice("d10")]
rDone[2] = rInhab[rollDice("d20")]
rDone[3] = longRuin[rollDice("d8")]
rDone[4] = rCondition[rollDice("d10")]

# Random Number for getting town name.
randNum = random.randint(0, 306)

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
ttk.Button(mainframe, text="Generate!", command=generate).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Random Town", justify='right').grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Ruin Name", justify='right').grid(column=1, row=1, sticky=W)

# Show result of random name grabbed.
townResult = StringVar(mainframe, townName[randNum])
ttk.Label(mainframe, textvariable=townResult).grid(column=2, row=2, sticky=(W, E))

ttk.Radiobutton(mainframe, text="Choose this", variable=radChoose, value=1).grid(column=3, row=1, sticky=W)
ttk.Radiobutton(mainframe, text="OR choose this", variable=radChoose, value=2).grid(column=3, row=2, sticky=W)

town_entry.focus()
window.bind("<Return>", generate)

window.mainloop()
