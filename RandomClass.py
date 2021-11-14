# You are required to design a method in a class which generates random numbers. The method
# accepts the following variables as input (int amount, int minRange, int maxRange). The amount
# variable depicts how many random numbers will be returned, the minRange variable depicts the
# starting range of the random number and the maxRange variable depicts the maximum number
# that the random number could be.

import random


class RandomNum:
    def __init__(self, minRange, maxRange, amount):
        self.minRange = minRange
        self.maxRange = maxRange
        self.amount = amount

    def printRandom(self):
        rand_list = [random.randint(self.minRange, self.maxRange) for _ in range(self.amount)]
        return rand_list

    @classmethod
    def get_user_input(self):
        try:
            self.minRange = int(input('Enter the minimum possible random number: '))
            self.maxRange = int(input('Enter  the maximum possible random number: '))
            self.amount = int(input('Enter the number of random numbers to be returned: '))
        except:
            print("Invalid input")


attempt1 = RandomNum.get_user_input()
attempt1.printRandom
