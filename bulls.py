import random
import sys

class MyRandomizer:
    def __init__(self):
        """ Initialize randomize
        """
        self._number = None

    def setNumber(self, number):
        """ Override the random feature and set the number
        so that it's always the same

        @param number Number to return (as string)
        """
        self._number = number

    def getNumber(self):
        """ Get random 4 digit number which contains only one number once.
        For example 9999 is invalid but 9876 is valid.

        @returns Four digit number (or the overridden number) as a string
        """
        if self._number!=None:
            return self._number
        nums = range(10)
        random.shuffle(nums)
        return "".join([str(x) for x in nums[:4]])


class BullsCowsGame:
    def __init__(self, randomizer=MyRandomizer()):
        """ Initialize the game and get the number to guess.

        @param randomize Randomizer class which should return 4 digit number (as string) when called it's getNumber() method.
        """
        self._randomizer = randomizer
        self._number = self._randomizer.getNumber()

    def bullCow(self, a, b):
        """ Return number of bulls and cows.
        https://en.wikipedia.org/wiki/Bulls_and_cows
        
        @param a Correct answer
        @param b User's guess
        @return Tuple containing bulls and cows
        """
        bulls = sum(map(lambda x,y: 1 if (x==y) else 0, a,b))
        cows = sum(map(lambda x,y: 1 if x!=y and x in b else 0, a,b))
        return (bulls, cows)

    def checkAnswer(self, guess):
        """ Checks whether the answer is correct.

        @param guess User's guess
        @return True if right, otherwise a hint message
        """
        if self._number == guess: return True

        (bulls, cows) = self.bullCow(self._number, guess)
        if bulls==len(self._number): return True

        return "Bulls: %s, Cows: %s"%(bulls,cows)

    def prompt(self):
        print "Your guess:"


if __name__=="__main__":
    b = BullsCowsGames()
    while True:
        b.prompt()
        ans = sys.stdin.readline().strip()
        if ans == None or ans == "":
            sys.exit(0)
        res = b.checkAnswer(ans):
        if res == True:
            print "Correct!"
            sys.exit(0)
        print res
