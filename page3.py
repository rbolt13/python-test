#lists
print("Let's look at some lists.")
list = ["MTH300", "STAT361", "GEOG380U", "MTH311", "STAT363", "SYSC 334U"]
txt = "Here is a list of my class schedule for 2021 : {}"
print(txt.format(list))
z = (len(list))
txt = "There are {} items in this list"
print(txt.format(z))
z = (list[2])
txt = "The second item on the list is {}"
print(txt.format(z))
z = (list[-2])
txt = "The -2 item on the list is {}"
print(txt.format(z))
z = (list[2:5])
txt = "Items between 2 and 5 are {}"
print(txt.format(z))
print("\n")

print("Nice work. Now lets look at some facts about strings.")
list1 = ["abc", 34, True, 40, "male"]
txt = "Let list 1 be different variables: {}"
print(txt.format(list1))
print(type(list1))
list2 = 2, 2, 2, 2, 2
txt = "Let list 2 be all the same value: {}"
print(txt.format(list2))
print(type(list2))

print("\nNeato! Lets take a few notes about arrays before we move on.\n")

print("A list is a collection which is ordered and chageable. Allows duplicate members.")
print("A tuple is a collection which is ordered and unchangeable. Allows duplicate members.")
print("A set is a collection which is unordered and unindexed. No duplicate members. ")
print("A dictionary is a collection which is unordered and changeable. No duplicate members.")
print("\n")

print("Let's change an change the second item on list1 above to female")
list1[2] = "female"
print(list1)
print("Actually let's change the entire middle section of that list.")
list1[1:4] = ["xyz", "qrt"]
print(list1)
print("Changed my mind lets put female back.")
list1.insert(1, "female")
print(list1)
print("And add orange")
list1.append("orange")
print(list1)
print("Dont forget apple, to the right of female.")
list1.insert(2,"apple")
print(list1)
print("Now lets combine list1 and the list of my classes")
list1.extend(list)
print(list1)
print("Okay let's remove that abc.")
list1.remove("abc")
print(list1)
print("and the qrt.")
list1.pop(3)
print(list1)
print("and the last item.")
list1.pop()
print(list1)
print("and the xyz.")
del list1[2]
print(list1)
print("Did you remember list2? Me neither. Let's delete it, and clear list 1")
del list2
list1.clear()
print("/n")
