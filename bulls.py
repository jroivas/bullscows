import random
import sys

class MyRandomizer:
    def __init__(self, number = None):
        """ Initialize randomize
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
    """ Bulls and Cows game
        https://en.wikipedia.org/wiki/Bulls_and_cows

    >>> b = BullsCowsGame(randomizer=MyRandomizer("1234"))
    >>> b.checkAnswer("1234")
    True
    >>> b.checkAnswer("1235")
    (3, 0)
    >>> b.checkAnswer("1203")
    (2, 1)
    >>> b.checkAnswer("0023")
    (0, 2)
    >>> b.checkAnswer("0000")
    (0, 0)
    >>> b.checkAnswer("1111")
    (1, 0)
    >>> b.checkAnswer("1")
    Invalid input!
    (0, 0)
    >>> b.checkAnswer("11234")
    Invalid input!
    (0, 0)
    >>> b.handleGuess("1234")
    Correct!
    True
    >>> b.handleGuess("1233")
    Bulls: 3, Cows: 0
    False
    >>> b.checkAnswer("9999")
    (0, 0)
    >>> b = BullsCowsGame(randomizer=MyRandomizer("9999"))
    >>> b.checkAnswer("9999")
    True
    >>> b.prompt()
    Your guess:
    >>> b.bullCow("7890","1234")
    (0, 0)
    >>> b.bullCow("7890","0914")
    (0, 2)
    >>> b.bullCow("7890","9876")
    (1, 2)
    >>> b.bullCow("7890","0987")
    (0, 4)
    >>> b.bullCow("7890","0890")
    (3, 0)
    >>> b.bullCowAlternative("7890","1234")
    (0, 0)
    >>> b.bullCowAlternative("7890","0914")
    (0, 2)
    >>> b.bullCowAlternative("7890","9876")
    (1, 2)
    >>> b.bullCowAlternative("7890","0987")
    (0, 4)
    >>> b.bullCowAlternative("7890","0890")
    (3, 0)
    """
    def __init__(self, randomizer=MyRandomizer(), useAlternative=False):
        """ Initialize the game and get the number to guess.

        @param randomize Randomizer class which should return 4 digit number (as string) when called it's getNumber() method.
        """
        self._randomizer = randomizer
        self._number = self._randomizer.getNumber()
        self._useAlternative = useAlternative

    def bullCow(self, a, b):
        """ Return number of bulls and cows.
        
        @param a Correct answer
        @param b User's guess
        @return Tuple containing bulls and cows
        """
        if len(a)!=len(b):
            print "Invalid input!"
            return (0,0)
        bulls = sum(map(lambda x,y: 1 if (x==y) else 0, a,b))
        cows = sum(map(lambda x,y: 1 if x!=y and x in b else 0, a,b))
        return (bulls, cows)

    def bullCowAlternative(self, a, b):
        """ Alternative way to return number of bulls and cows.
        This is powerful one liner!
        
        @param a Correct answer
        @param b User's guess
        @return Tuple containing bulls and cows
        """
        if len(a)!=len(b):
            print "Invalid input!"
            return (0,0)
        bulls,cows = zip(*[(1,0) if i==j else (0,1) if j in a and b.count(j)==1 else (0,0) for i,j in zip(a,b)])
        return (sum(bulls), sum(cows))

    def checkAnswer(self, guess):
        """ Checks whether the answer is correct.

        @param guess User's guess
        @return True if right, otherwise bulls and cows count
        """
        if self._number == guess: return True

        if self._useAlternative:
            (bulls, cows) = self.bullCowAlternative(self._number, guess)
        else:
            (bulls, cows) = self.bullCow(self._number, guess)
        if bulls==len(self._number): return True
        return (bulls, cows)

    def prompt(self):
        """ Prompt user
        """
        print "Your guess:"

    def handleGuess(self, guess):
        """ Handle a user guess

        @param guess User's guess
        @return True if correct, False otherwise
        """
        res = self.checkAnswer(guess)
        if res == True:
            print "Correct!"
            return True
        print "Bulls: %s, Cows: %s"%res
        return False

if __name__=="__main__":
    b = BullsCowsGame(useAlternative=True)
    while True:
        b.prompt()
        ans = sys.stdin.readline().strip()
        if ans == None or ans == "":
            sys.exit(0)
        if b.handleGuess(ans):
            sys.exit(0)
