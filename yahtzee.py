"""
This is will eventually be the game of yahtzee.
For now, it outputs and saves the roll of six dice.
-----------------------------------------------
Sources :

Write Yahtzee in Python :
https://colab.research.google.com/drive/1I_0h72NlXz7YH29FES0qNyus_NvlsPV2
https://stackoverflow.com/questions/44008489/dice-rolling-simulator-in-python/44009898

"""
"""
import random

print("Welcome to Yahtzee")

txt = "Your first roll is {}, {}, {}, {}, {}, {}"

die1 = random.randint(1,6)
die2 = random.randint(1,6)
die3 = random.randint(1,6)
die4 = random.randint(1,6)
die5 = random.randint(1,6)
die6 = random.randint(1,6)

print(txt.format(die1, die2, die3, die4, die4, die5, die6))

"""
import random
random.randint(1,6)
def rollDice(n):
  rolls = [random.randint(1,6) for i in range (n)]
  return rolls

currRolls = rollDice(5)
print(currRolls)

counts = [currRolls.count(1), currRolls.count(2),currRolls.count(3), currRolls.count(4), currRolls.count(5), currRolls.count(6)]
print(counts)

maxCount = max(counts)
print (maxCount)

maxVal = counts.index(maxCount)
print(maxVal+1)
