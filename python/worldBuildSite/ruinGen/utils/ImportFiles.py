import os

class importFiles():

    def villPre():
        vPre = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/worldBuildSite/ruinGen/utils/contentFiles/Village_Prefixes.txt'
    
        with open(vPre) as fPre:
            preVill = fPre.read().splitlines()
            fPre.close()
        return preVill

    def villSuf():
        vSuf = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/worldBuildSite/ruinGen/utils/contentFiles/Village_Suffixes.txt'

        with open(vSuf) as fSuf:
            sufVill = fSuf.read().splitlines()
            fSuf.close()
        return sufVill

    def villType():
        vType = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/worldBuildSite/ruinGen/utils/contentFiles/VillageType.txt'

        with open(vType) as fType:
            typeVill = fType.read().splitlines()
            fType.close()
        return typeVill

    def villShop():
        vShop = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/worldBuildSite/ruinGen/utils/contentFiles/VillageShops.txt'

        with open(vShop) as fShop:
            shopVill = fShop.read().splitlines()
            fShop.close()
        return shopVill

    def villAge():
        vAge = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/worldBuildSite/ruinGen/utils/contentFiles/Village_Age.txt'

        with open(vAge) as fAge:
            ageVill = fAge.read().splitlines()
            fAge.close()
        return ageVill

    def villGov():
        vGov = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/worldBuildSite/ruinGen/utils/contentFiles/Village_Gov.txt'

        with open(vGov) as fGov:
            govVill = fGov.read().splitlines()
            fGov.close()
        return govVill

    def rStruct():
        ruinAtt = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            rStruct = fAtt.read().splitlines()[1:11]
            fAtt.close()
        return rStruct

    def rInhab():
        ruinAtt = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            rInhab = fAtt.read().splitlines()[13:33]
            fAtt.close()
        return rInhab

    def yRuin():
        ruinAtt = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            yRuin = fAtt.read().splitlines()[35:45]
            fAtt.close()
        return yRuin

    def longRuin():
        ruinAtt = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            lRuin = fAtt.read().splitlines()[47:55]
            fAtt.close()
        return lRuin

    def rCondition():
        ruinAtt = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/contentFiles/Ruin_Attributes.txt'

        with open(ruinAtt) as fAtt:
            rCondition = fAtt.read().splitlines()[58:68]
            fAtt.close()
        return rCondition

    def townName():
        nTown = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/contentFiles/Town_Names.txt'

        with open(nTown) as fTown:
            tName = fTown.read().splitlines()
            fTown.close()
        return tName
    
    def townGeo():
        gTown = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/contentFiles/Settlement_Geography.txt'

        with open(gTown) as fGeo:
            tGeo = fGeo.read().splitlines()
            fGeo.close()
        return tGeo

    def govType():
        gType = 'C:/Users/' + os.environ['USERNAME'] + '/Documents/GitHub/Projects/python/contentFiles/GovType.txt'

        with open(gType) as fGov:
            tGeo = fGov.read().splitlines()
            fGov.close()
        return tGeo

# For Testing purposes
# print(importFiles.rStruct())
# print(importFiles.rInhab())
# print(importFiles.yRuin())
# print(importFiles.longRuin())
# print(importFiles.rCondition())
# print(importFiles.villSize())
# print(importFiles.townGeo())
# print(importFiles.villAge())