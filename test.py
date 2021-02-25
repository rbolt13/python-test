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
k = 'as sinlge quotes'

print(j)
print(k)

A = "\nVariable names are case-sensitive.\n"
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

a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)
