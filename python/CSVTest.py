import csv, os


#with open(filename) as f:
#    mylist = f.read().splitlines()

resultFile = 'C:/Users/scott/Downloads/Village_Prefixes.txt'

with open(resultFile) as f:
    preVill = f.read().splitlines()

print(preVill)