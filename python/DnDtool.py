from tkinter import *
from tkinter import ttk
import random

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


randNum = random.randint(0, 100)

window = Tk()
window.title("DnD Tool")

mainframe = ttk.Frame(padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)


radChoose = IntVar()
radChoose.set(1)
# E1 = Entry()
# E1.pack(side = RIGHT)

nameTown = StringVar()
town_entry = ttk.Entry(mainframe, width=7, textvariable=nameTown)
town_entry.grid(column=2, row=1, sticky=(W, E))

# greeting = Label(window, text=townName[randNum])
# greeting.pack(side = LEFT)

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=1, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Generate!" ).grid(column=3, row=3, sticky=W) #, command=<inser function>

ttk.Label(mainframe, text="Random Town").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Ruin Name").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text=townName[randNum]).grid(column=2, row=2, sticky=(W, E))

ttk.Radiobutton(mainframe, variable=radChoose, value=1).grid(column=3, row=1)
ttk.Radiobutton(mainframe, variable=radChoose, value=2).grid(column=3, row=2)

#for child in mainframe.winfo_children(): 
#    child.grid_configure(padx=5, pady=5)

town_entry.focus()
# window.bind("<Return>", <insert function>)

window.mainloop()