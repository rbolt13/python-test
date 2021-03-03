# 4 built-in data types in Python are : Tuple, List, Set, and Dictionary

# Tuples : used to store multiple items in a single variable

print("Lets being by printing thistuple!")
thistuple = ("apple", "banana","apple", "cherry")
print(thistuple)

#Tuple itesm are ordered, unchagebale, and allow duplicate values.
#The first index [0], the second item has an index [1]

z = len(thistuple)
txt = "The length of thistuple is : {}"
print(txt.format(z))

z=type(thistuple)
txt = "thistuple is of type : {}"
print(txt.format(z))

print("The second item of thistuple is : ")
print(thistuple[1])

# Tuple Items can be of data type :
# string, boolean, int, and varying types of data

print("\nLet's print some more tuple's")
tuple1 = (1, 5, 7, 9, 3)
tuple2 = (True, False, False)
tuple3 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1))
print(tuple2)
print(type(tuple2))
print(tuple3)
print(type(tuple3))

print("Next we are going to convert a tuple into a changeable list.")
x = ("apple", "banana", "cherry")
y = type(x)
txt=("Lets start with tuple : {}, of {}")
print(txt.format(x,y))

print("Now let's replace banana with cherry and change the type to tuple")
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print(type(x))
print("We can add items to the end of our tuple and then convert back to tuple:")
y = list(x)
y.append("orange")
thistuple = tuple(y)
print(y)
print("And delete items, like apple :")
y= list(thistuple)
y.remove("apple")
thisuple = tuple(y)
print(y)
del thistuple

#unpacking a tuple
txt = "lets begin by unpacking our tuple {} : "
fruits = x
(green, yellow, red) = fruits
print(txt.format(fruits))
print(yellow)
print(green)
print(red)

"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

"""
#Loops
txt="\nNow let's use a loop to print {}"
thistuple = ("apple", "banana", "cherry")
print(txt.format(thistuple))
for x in thistuple:
  print(x)

print("\nagain with an index")
for i in range(len(thistuple)):
    print(thistuple[i])

print("\nand a while loop")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i +1

#Join Tuples
print("\nNow lets add two tuples!")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiple Tuples
print("\nLets multiple thistuple by 2")
thistuple = fruits*2
print(thistuple)

"""
Tuple Methos
count() : Return the number of times a speified value occurs in a tuple
index() : searches the tuple for a specified valued and returns the
            position of where it was found
"""

#Sets
print("\nNow lets print a set using curly brackets instead of parentheses")
#Duplicates not allowed
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))
print(len(thisset))
#set can use differet data types and varying data types

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#for loop
for x in thisset:
    print(x)
print("\nIs banana in thisset?")
print("banana" in thisset)
print("\nLets add orange to thisset")
thisset.add("orange")
print(thisset)
#.update()
print("\nAdd the tropical set to thisset")
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
print("\nAnd the tuple mylist")
mylist = ["kiwi", "strawberry"]
thisset.update(mylist)
print(thisset)
# .remove and .discard
print("\nNow lets remove some things")
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)
#.pop()
txt = "\nAnd with the pop() method we will remove {}"
x = thisset.pop()
print(txt.format(x))
print(thisset)

"""
to delete or clear set
thisset.clear()
del thisset
"""
#.union()
print("\nTime to play around with union()")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#.update()
print("\nAgain but with update()")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#.intersection_update()
print("\nFind common items that exist for both sets")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#.intersection()
print("\nOr create a new list from those items")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
#.symmetric_difference_update()
print("\nKeep the items that are present in both sets")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#.symmetric_difference()
print("\nAgain but creating a new set")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
"""
Set Methods:
add()
clear()
copy()
difference()
difference_update()
discard()
intersection()
intersection_update()
isdisjoint()
issubset()
pop()
remove()
symmetric_difference()
symmetric_difference_update()
union()
update()
"""
#Dictionary : Used to store data values in key: value pairs
#Ordered, changeable, and does not allow duplicates

print("\nLet's switch gears and create and print a dictionary: ")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#print value of "brand"
print(thisdict["brand"])
#print length
print(len(thisdict))
#print type
print(type(thisdict))

#Can use strings, int, boolean, and list data types
