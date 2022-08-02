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