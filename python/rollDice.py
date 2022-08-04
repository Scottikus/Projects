import random

class rollDice():

    def d20():
        r = random.randint(0, 19)
        return r

    def d12():
        r = random.randint(0, 11)
        return r

    def d10():
        r = random.randint(0, 9)
        return r

    def d8():
        r = random.randint(0, 7)
        return r

    def d6():
        r = random.randint(0, 5)
        return r

    def d4():
        r = random.randint(0, 3)
        return r

    def d100():
        r = random.randint(0, 99)
        return r

    def d50():
        r = random.randint(0, 49)
        return r

    def villSize(vType: str):
        if vType == "Thorp":
            rSize = str(random.randint(20, 80))
            return rSize
        elif vType == "Hamlet":
            rSize = str(random.randint(81, 400))
            return rSize
        elif vType == "Village":
            rSize = str(random.randint(401, 900))
            return rSize
        elif vType == "Small Town":
            rSize = str(random.randint(901, 2000))
            return rSize
        elif vType == "Large Town":
            rSize = str(random.randint(2001, 5000))
            return rSize
        elif vType == "Small City":
            rSize = str(random.randint(5001, 12000))
            return rSize
        elif vType == "Large City":
            rSize = str(random.randint(12001, 25000))
            return rSize
        elif vType == "Metropolis":
            rSize = "25001+"
            return rSize
    
    def villBiz(vType: str):
        if vType == "Thorp":
            rBiz = "0"
            return rBiz
        elif vType == "Hamlet":
            rBiz = str(random.randint(1, 2))
            return rBiz
        elif vType == "Village":
            rBiz = str(random.randint(2, 3))
            return rBiz
        elif vType == "Small Town":
            rBiz = str(random.randint(3, 4))
            return rBiz
        elif vType == "Large Town":
            rBiz = str(random.randint(5, 8))
            return rBiz
        elif vType == "Small City":
            rBiz = str(random.randint(10, 20))
            return rBiz
        elif vType == "Large City":
            rBiz = str(random.randint(25, 40))
            return rBiz
        elif vType == "Metropolis":
            rBiz = "40"
            return rBiz














