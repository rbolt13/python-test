a = "Hello User! \nThis program goes over some basic python."
b = "Let's begin\n"
print(a)
print(b)

print("Is 5 > 2?")

if 5 > 2:
    print("Five is greater than two!\n")

#casting
x = str(3)
y = int(3)
z = float(3)

print(x,y,z)
print(type(x),type(y),type(z))

j = "\ndouble quotes are the same"
k = 'as sinlge quotes\n'

print(j)
print(k)

A = "Variable names are case-sensitive.\n"
print(A)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Cherry"
print(x)
print(y)
print(z)

x = "awesome"
print("\nPython is "+x)

x = "Python "
y = "is"
z = x + y
print(z)

x = 20
y = 80
z = x + y
print(z)

x = "awesome"

def myfunc():
    print("Randi is " +x)

myfunc()

def myfunc():
    global x
    x = "fantastic\n"

myfunc()

print("Python is " + x)

def deftype():
    print(x,y,z)
    print(type(x),type(y),type(z))
    print("\n")

#int , float, complex
x = 1
y = 2.8
z = 1j
deftype()
#int
x = 1
y = 35656222554887711
z = -3255522
deftype()
#float
x = 1.10
y = 1.0
z = -35.59
deftype()
#float
x = 35e3
y = 12E4
z = -87.7e100
deftype()
#complex
x = 3+5j
y = 5j
z = -5j
deftype()

x = 1 # int
y = 2.8 # float
z = 1j # complex
print(x,y,z)
print(type(x),type(y),type(z))
a = float(x) # convert from int to float
b = int(y) # convert from float to int
c = complex(x) #convert int to complex
print(a,b,c)
print(type(a),type(b),type(c))
print("\n")


import random
print("Here is a random number between 1 and 10: ")
print(random.randrange(1,10))

print("\nTime for some strings!")
a = "Hello, World! "
print("Variable a = " + a)
print("The second letter of a is " + a[1])
print("The letters between 2 and 5 are " +a[2:5])
print("The characters from the 2nd position to the end are " + a[2:])
print("Characters from the start position to 5(not included) are " + a[:5])
print("The characters from position -5 (o in world) to")
print("(but not included) -2 (d in world) are "+a[-5:-2])
print("The length of a is ")
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H","J"))
print(a.split(","))
print("\n")

print("Is 'free in the mystery txt?'")
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
print("Is expensive? NOT in the mystery txt?")
print("expensive" not in txt)
if "expensive" not in txt:
    print("'expensive' is NOT present")
print("\n")

a = "No"
b = "Space"
c = a + b
print(c)
c = a + " " + b
print(c)
print("\n")

age = 27
txt = "My age is {}"
print(txt.format(age))
print("\n")

q = 3
i = 567
p = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(q,i,p))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(q,i,p))
print("\n")

txt = "I once was a \"young warthog\""
print(txt)
txt = "Hello\tTab!"
print(txt)
print("\n")

#Boolean Values
print("Is 10 > 9?")
print(10 > 9)
print("Is 10 = 9?")
print(10 == 9)
print("Is 10 < 9?")
print(10 < 9)
print("Let a = 200 and b = 33")
a = 200
b = 33
print("\n")

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print("\n")

print("Evaluate \"Hello\"")
print(bool("Hello"))
print("Evalute 15")
print(bool(15))
print("Evaluate a = 200 (from above).")
print(bool(a))
print("\n")

print("Any string is True except for empty strings.")
print("Any number is true, except 0.")
print("Any list, tuple, set, and dictionary are true except empty ones.")
print("\n")

print("Here are some True Values")
print("abc",bool("abc"))
print("123",bool(123))
print("[\"apple\", \"cherry\", \"banana\"]", bool(["apple", "cherry", "banana"]))
print("\n")

print("Here are some False Values")
print("\"False\"", bool(False))
print("None",bool(None))
print("0",bool(0))
print("\"\"",bool(""))
print("[]", bool([]))
print("{}", bool({}))
print("\n")

print("Here is a function that returns a Boolean Value.")
def myFunc():
    return True
print(myFunc())
print("_len_ function returns 0 or false:")
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
print("Code based on a Boolean function that tells if :")
if myFunc():
    print("YES!")
else:
    print("NO!")
print("\n")

print("Check if an object is an integer or not")
print(isinstance(a, int))
