# Import necessary libraries
from tkinter import *
from tkinter import ttk
import random
import os
from rollDice import *
from ImportFiles import *

#def build():
numCountries = random.randint(5, 8)
biome = 'none'

biomes = [['Tundra','Tundra','Temperate Grassland','Temperate Grassland','Temperate Grassland','Desert','Desert','Desert']
,['Tundra','Boreal Forest','Boreal Forest','Woodland','Woodland','Savanna','Desert','Desert']
,['Tundra','Boreal Forest','Boreal Forest','Temperate Dry Forest','Temperate Dry Forest','Savanna','Savanna','Desert']
,['Tundra','Boreal Forest','Boreal Forest','Temperate Dry Forest','Temperate Dry Forest','Savanna','Savanna','Savanna']
,['Tundra','Tundra','Temperate Rainforest','Temperate Rainforest','Temperate Rainforest','Tropical Rainforest','Savanna','Savanna']
,['Tundra','Tundra','Swamp','Swamp','Temperate Rainforest','Tropical Rainforest','Tropical Rainforest','Savanna']
,['Tundra','Swamp','Swamp','Swamp','Swamp','Tropical Rainforest','Tropical Rainforest','Tropical Rainforest']
,['Tundra','Swamp','Swamp','Swamp','Swamp','Tropical Rainforest','Tropical Rainforest','Tropical Rainforest']]

countries = []

for x in range(numCountries):
    rain = rollDice.d8()
    temp = rollDice.d8()
    biome = biomes[temp][rain]
    countries.append(biome)


print(numCountries)
print(countries)








#Number of Countries


#Biome generation

#Village Number gen
