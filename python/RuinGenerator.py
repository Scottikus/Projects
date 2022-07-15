#Ruin Generator
# I am creating a prompt to create a ruined place for Dnd to practice Python Code!

#Dice Roll function
import random

rStruct = [
    "A small collection of huts"
    , "A grand noble’s manor"
    , "A temple or monastery"
    , "A mighty citadel"
    , "A single cottage"
    , "A once mighty wizard’s tower"
    , "A cemetary or tomb"
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

rDone = ["", "", "", "", ""]

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

print("Welcome to Ruin Generator!")
print("What would you like to start with?")

y = 1
while y < 6:
    print("1. Ruin Structure")
    print("2. Why was it ruined?")
    print("3. Current Inhabitants")
    print("4. How long ago was it ruined?")
    print("5. Ruin Condition?")

    #input from variables needs to be specified 

    options = int(input())

    #Case statements don't exist. if elseif and else instead

    if options == 1:

        rDone[0] = rStruct[rollDice("d10")]
        print(rDone[0])
    elif options == 2:
        rDone[1] = yRuin[rollDice("d10")]     
        print(rDone[1])
    elif options == 3:
        rDone[2] = rInhab[rollDice("d20")]
        print(rDone[2])
    elif options == 4:
        rDone[3] = longRuin[rollDice("d8")]
        print(rDone[3])
    elif options == 5:
        rDone[4] = rCondition[rollDice("d10")]
        print(rDone[4])
    else:
        print("Sorry, that is not an option.")
    y = y + 1 #endWhile

print('What shall we call it?')

ruinName = input()

print('Okay it looks like your ruin is:\n' + 
rDone[0] + " that was ruined by " + rDone[1] + ".\nIt's current inhabitants are " 
+ rDone[2] + ".\nIt has been in ruins for " + rDone[3] + ".\nIt's condition is that it is " + rDone[4] + ".")

resultFile = 'C:/Users/scott/Downloads/RuinedPlaces.txt'

with open (resultFile, 'a') as file_object:
    
    file_object.write(ruinName + " is " + rDone[0] + " that was ruined by " + rDone[1] + ".\nIt's current inhabitants are " 
                      + rDone[2] + ".\nIt has been in ruins for " + rDone[3] + ".\nIt's condition is that it is " + rDone[4] + ".")
    file_object.write('\n')
    
    #for ruins in rDone:
    #    file_object.write(ruins + "\n")
    #file_object.write('\n')

print('Ruin has been saved to the RuinedPlaces file!')
