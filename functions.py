"""
Functions
"""

def my_function():
    print("Time for functions in python.")

my_function()

"""
Arguments (Parameters)
Information can be passed into functions as arguments.
The value that is sent to the function when it is called.
"""

def my_function(type):
  print(type + " Power")

my_function("Girl")
my_function("Flower")
my_function("Rocket")
print("\n")

def my_function(fname, lname): #function expects 2 arguments
  print(fname + " " + lname)

my_function("Randi", "Bolt")
print("\n")

#Arbitrary Arguments, *args
#Use this # of argumnets passing through is unknown
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
print("\n")

#keyword arguments or kwargs
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print("\n")

#Arbitrary Keyword Arguments, **kwargs
#Don't know how many keyword aruments that will be passed

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
print("\n")

#Default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print("\n")

#Passing a List as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
print("\n")

#Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
print("\n")

#pass
def myfunction():
  pass


#Recursion : a defined function can call itself
### Be carful, recursion can be easy to slip into functions that never terminte
def tri_recursion(k):
  if(k > 0): # k is variable as the data
    result = k + tri_recursion(k - 1) # k decrements by -1 every recurse
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
print("\n")

"""
Lambda is a small anonymous function
Syntax
lambda arguments : expression
"""
x = lambda a : a + 10
print(x(5))
print("\n")

x = lambda a, b : a * b
print(x(5, 6))
print("\n")

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
print("\n")

#Use when an argument will be multiplied with an unknown number
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(11))
#same function but triples of it
mytripler = myfunc(3)

print(mytripler(11))

#written together
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
