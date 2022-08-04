

class importFiles():

    def villPre():
        vPre = 'python/contentFiles/Village_Prefixes.txt'
    
        with open(vPre) as fPre:
            preVill = fPre.read().splitlines()
            fPre.close()
        return preVill

    def villSuf():
        vSuf = 'python/contentFiles/Village_Suffixes.txt'

        with open(vSuf) as fSuf:
            sufVill = fSuf.read().splitlines()
            fSuf.close()
        return sufVill

    def villType():
        vType = 'python/contentFiles/VillageType.txt'

        with open(vType) as fType:
            typeVill = fType.read().splitlines()
            fType.close()
        return typeVill

    def villShop():
        vShop = 'python/contentFiles/VillageShops.txt'

        with open(vShop) as fShop:
            shopVill = fShop.read().splitlines()
            fShop.close()
        return shopVill

    def rStruct():
        ruinAtt = 'python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            rStruct = fAtt.read().splitlines()[1:11]
            fAtt.close()
        return rStruct

    def rInhab():
        ruinAtt = 'python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            rInhab = fAtt.read().splitlines()[13:33]
            fAtt.close()
        return rInhab

    def yRuin():
        ruinAtt = 'python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            yRuin = fAtt.read().splitlines()[35:45]
            fAtt.close()
        return yRuin

    def longRuin():
        ruinAtt = 'python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            lRuin = fAtt.read().splitlines()[47:55]
            fAtt.close()
        return lRuin

    def rCondition():
        ruinAtt = 'python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            rCondition = fAtt.read().splitlines()[58:68]
            fAtt.close()
        return rCondition

    def townName():
        nTown = 'python/contentFiles/Town_Names.txt'

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
# print(importFiles.villSize())