

class importFiles():

    def villPre():
        vPre = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Village_Prefixes.txt'

        with open(vPre) as fPre:
            preVill = fPre.read().splitlines()
        return preVill

    def villSuf():
        vSuf = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Village_Suffixes.txt'

        with open(vSuf) as fSuf:
            sufVill = fSuf.read().splitlines()
            fSuf.close()
        return sufVill

    def rStruct():
        ruinAtt = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            rStruct = fAtt.read().splitlines()[1:10]
            fAtt.close()
        return rStruct

    def rInhab():
        ruinAtt = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            rInhab = fAtt.read().splitlines()[13:33]
            fAtt.close()
        return rInhab

    def yRuin():
        ruinAtt = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            yRuin = fAtt.read().splitlines()[36:45]
            fAtt.close()
        return yRuin

    def longRuin():
        ruinAtt = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            lRuin = fAtt.read().splitlines()[48:55]
            fAtt.close()
        return lRuin

    def rCondition():
        ruinAtt = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            rCondition = fAtt.read().splitlines()[59:68]
            fAtt.close()
        return rCondition

    def townName():
        nTown = 'C:/Users/scott/Documents/GitHub/Projects/python/contentFiles/Town_Names.txt'

        with open(nTown) as fTown:
            tName = fTown.read().splitlines()
            fTown.close()
        return tName


# For Testing purposes
# print(importFiles.rStruct())
# print(importFiles.rInhab())
# print(importFiles.yRuin())
# print(importFiles.longRuin())
# print(importFiles.rCondition())
