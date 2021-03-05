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
