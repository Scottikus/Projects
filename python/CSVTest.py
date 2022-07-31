#with open(filename) as f:
#    mylist = f.read().splitlines()

villPre = 'C:/Users/scott/Downloads/Village_Prefixes.txt'

with open(villPre) as f:
    preVill = f.read().splitlines()

print(preVill)

ruinAtt = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

with open(ruinAtt) as fAtt:
    rStruct = fAtt.read().splitlines()[1:10]

with open(ruinAtt) as fAtt:
    rInhab = fAtt.read().splitlines()[13:33]

with open(ruinAtt) as fAtt:
    yRuin = fAtt.read().splitlines()[36:45]

with open(ruinAtt) as fAtt:
    longRuin = fAtt.read().splitlines()[48:55]

with open(ruinAtt) as fAtt:
    rCondition = fAtt.read().splitlines()[59:68]


print(rStruct)
print(rInhab)
print(yRuin)
print(longRuin)
print(rCondition)