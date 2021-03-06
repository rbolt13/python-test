"""
This is will eventually be the game of yahtzee.
For now, it outputs and saves the roll of six dice. 
-----------------------------------------------
Sources :

Write Yahtzee in Python :
https://betterprogramming.pub/interview-questions-write-yahtzee-in-python-72695550d84e
"""

import random

print("Welcome to Yahtzee")

a = random.randrange(1,6)
b = random.randrange(1,6)
c = random.randrange(1,6)
d = random.randrange(1,6)
e = random.randrange(1,6)
txt = "You rolled : {} , {} , {} , {} , {}"
print(txt.format(a, b, c, d, e))

dice_list = (a, b, c, d, e)
print(type(dice_list))
print(dice_list)
