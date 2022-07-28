from operator import concat
import random

preVill = ["All", "Aller", "Alver", "Ar", "Ashe", "Axe", "Bal", "Bard", "Bear", "Bell", "Black", "Blue", "Bone", 
           "Coal", "Cold", "Cora", "Crown", "Crystal", "Dagger", "Dark", "Darrow", "Deep", "Dor", "Dragon", "Dry", 
           "Durn,", "Dust,", "East,", "Edge,", "Eld", "Ever,", "Fey", "Frey,", "Frost", "Gill,", "Gold,", "Grand", 
           "Green", "Grey,", "Grim,", "Hammer", "Haw", "High,", "Hol", "Ice", "Iron,", "Jewel", "Kel", "Kil", "King,", 
           "Lan", "Leaf,", "Lun", "Mal", "Marsh", "Mon", "Moon,", "Mor", "Mur", "Nether", "North", "Oak", "Old", 
           "Pan", "Pel", "Rain,", "Raven", "Red", "Rock,", "Rom", "Roth,", "Ruby,", "Rune,", "Salt,", "San", "Silver", 
           "South", "Star", "Stone", "Storm", "Strath", "Sun", "Tar", "Ten", "Tin", "Torr", "Tran", "Val", "Vine", 
           "West", "White", "Wild", "Willow", "Wim", "Wind", "Winter", "Witch", "Wolfen", "Yar", "Zel"]

sufVill = ["barrow", "bay", "bend", "bridge", "burgh", "burough", "bury", "cliff", "crest", "cress", "dale", "don", 
           "dorf", "end", "far", "fell", "field", "ford", "gate", "grave", "guard", "hall", "haven", "helm", "hill", 
           "holme", "land", "meet", "meadow", "mill", "moor", "mount", "point", "pool", "port", "rest", "shire", 
           "smith", "song", "spring", "stead", "stow", "tree", "town", "view", "wall", "watch", "well", "wich", "wood"]

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

test = rollDice('d100')

print('test = ')
print(test)

randNum1 = random.randint(0, 49)

name1 = preVill[rollDice('d100')]
name2 = sufVill[randNum1]
comboTown =  name1 + name2

print(name1)
print(name2)
print(comboTown)
