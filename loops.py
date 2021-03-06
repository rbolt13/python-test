#Conditions and If Statements
'''
Equals : a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''
a = 33
b = 200
if b > a:
     print("b is greater than a")
#Elif : "if the precious conditions were not true then try this condition"
b = 33
if b > a:
    print(" b is greater than a")
elif a ==b:
    print("a and b are equal")
#else anything that isn't caugth by the preceding conditions
a = 200
if b > a:
     print("b is greater than a")
elif a ==b:
    print("a and b are equal")
else:
    print("a is greater than b")
#OR
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
 #Short hand if statement
if a > b: print("a is greater than b")

#short hand if... else statement
#print("A") if a > b else print("B")
#^^^technique known as terary operators or conditional expressions
#print("A") if a > b else print("=") if a == b else print("B")

#AND
c = 500
if a > b and c > a:
  print("Both conditions are True")
#OR
if a > b or a > c:
    print("At least one of the conditions is True")

#Nested If
txt = "\nHow about a nested statement about x = {}"
x = 41
print(txt.format(x))
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#pass : avoids getting error
if b > a:
    pass

#while loops
print("\nLet's print 1 - 5 with a while loop.")
i = 1
while i < 6:
  print(i)
  i += 1
#break
print("\nNow let's break when the look i is 3.")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i +=1
#continue the next iterartion if i is 3
print("\nAnd continue again starting with i = 3.")
i = 3
while i < 6:
    i+= 1
    if i == 3:
        continue
    print(i)
#Else
print("\nPrint a message once the condition is false")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

 #For loops
print("\nPrint each fruit in the list.")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

 #break : Notice the first case stops after banana and the second stops before.
print("\nStop the loop before it goes through all the items. ")
for x in fruits:
  print(x)
  if x == "banana":
    break
print("\nStop the loop before it goes through all the items. ")
for x in fruits:
  if x == "banana":
    break
  print(x)

#continues
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Looping a string
print("\nLoop through the letters of the word banana.")
for x in "banana":
  print(x)

#range
for x in range(6):
    print(x)

for x in range(2,6):
    print(x)

#increase by value of 3
for x in range(2,30, 3):
    print(x)

#Else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#break when range is 3
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pass
for x in [0, 1, 2]:
  pass
