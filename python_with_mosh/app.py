#print name
print("Randi Bolt")

#print dog
print("o----")
print(" | | | |")

#python prints one line at a time in consecutive order

#here we are multiplying string by 10
#this line of code (EXPRESSION) prints **********
print('*'*10)

#this prints a heart
print("  *     *")
print('*   * *   *')
print(" *   *   * ")
print("   *   *")
print("    * *")
print(' '*5+'*')

#If you want to be a web developer would want HTML, CSS, JAVA and Jango
#jango is popular for building web applications

#allocates memory to 10 labeled price
price = 10
print(price)

#pyton updates line to line
price = 20
print(price)

#int is a number w/o decimal point
#float has decimal
#string
#boolean : yes / no

rating = 4.9
name = 'Randi'

#python is case sensitive, python wont understnad this with a lower case F
is_published = False
print(price)

name = 'John Smith'
age = 20
new_patient = True

#input is another operation like print
name = input('What is your name? ')
print('Hi '+ name)

#inputs and prints users names and a color they like
name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name + ' likes ' + color)

"""
This will give an error because whatever you type in
the terminal is always considered a string

birth_year = input('Birth Year: ')
age = 2021 - birth_year
print(age)
"""

birth_year = input('Birth Year: ')
age = 2021 - int(birth_year)
print(age)
print(type(birth_year))
print(type(age))

#converts weight in pounds to kilograms
weight_lbs = input('What is your weight in pounds? ')
weight_kg = 0.45359237*int(weight_lbs)
print(weight_kg)

#using "" vs ''
course = "Python's for Beginners"
print(course)
course = 'Python for "Beginners"'
print(course)

#multiple line string
course = '''
Hello class,
Here is our first email.
Thank you,
The support team
'''
print(course)
#understand syntax of []
course = "Pythons for Beginners"
print(course[0])

#negative charcter starts from the end
print(course[-1])

#print Pyt , stops and excludes character at 3
print(course[0:3])

#runs until the end of the string if left open
print(course[8:])

#simlar
print(course[:8])

 #prints entire string
print(course[:])

#prints all characters starting from e and ending at e
name = 'Jennifer'
print(name[1:-1])

#print --> John [Smith] is a coder
#this isn't ideal because message has to be visualized by user
first_name = 'John'
last_name = 'Smith'
message = first_name + '[' + last_name + '] is a coder'
print(message)

#formatted string
msg = f'{first_name} [{last_name}] is a coder'
print (msg)

#string methods
#len function can enforce limit on imput
course = "Python for Beginners"
print(len(course))
#functions called methods (in object oriented)
#len is a general purpose function
#.upper is a method because it belongs to a string
print(course.upper())
print(course.lower())
#print index # of 'P'
print(course.find('P'))
#case sensitive , so O will return -1 because it doens't exist
print(course.find('O'))
#replace
print(course.replace('Beginners', "Absolute Beginners"))
#does the string contain the word python
#this returns boolean true
#in operator produces boolean value
print('Python' in course)

""" recap
len()
course.upper()
course.lower()
course.title()
coure.find()
course.replace()
'...' in course
"""
