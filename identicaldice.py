# #! /usr/bin/env python3.11
# A simulation to determine the amount of tries it takes for a set of dice to all roll the same number
# By hypnotics | Started on 2/02/23 Completed on 02/02/23
# File Type: Simulation 

import random
import time

def main():
    user = int(input("Would you like to use the comparer method (1) or sum (2)\n> "))
    start_time = time.time()
    tries = 1 
    if user == 1:
        while True:
            if comparer(roller()) == True:
                print(f"It took {tries} amount of rolls to find the max, found in {time.time() - start_time} seconds")
                break
            tries += 1
    if user == 2:
        while True:
            if sum(roller()) == True:
                print(f"It took {tries} amount of rolls to find the max, found in {time.time() - start_time} seconds")
                break
            tries += 1

def roller() -> list[int]:
    """Rolls a set of dice, returns the output in the order ==>
    d4 d6 d8 d10 d12 d20"""
    return [random.randint(1,4), random.randint(1,6),random.randint(1,8),random.randint(1,10), random.randint(1,12), random.randint(1,20)]

def comparer(set: list[int]) -> bool:
    """Compare a given set, returns a bool"""
    dice_max = [4,6,8,10,12,20]
    for i in range(len(set)):
        if set[i] != dice_max[i]: return False
    return True

def sum(set: list[int]) -> bool:
    """Finds the sum, if the sum is equal to the max, returns True"""
    total = 0
    for i in set: total += i
    if total == 60: return True
    return False

if __name__ == "__main__":
    main()
