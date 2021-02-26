#Python Operations
print("Here are some Python operations!")
x = 10
y = 5
print("Let x = 10 and y = 5. ")
z = 10 + 5
txt = "x + y = {}"
print(txt.format(z))
z = 10 - 5
txt = "x - y = {}"
print(txt.format(z))
z = 10 * 5
txt = "x * y = {}"
print(txt.format(z))
z = 10 / 5
txt = "x / y = {}"
print(txt.format(z))
z = 10 % 5
txt = "x % y = {}"
print(txt.format(z))
z = 10 ** 5
txt = "x ** y = {}"
print(txt.format(z))
z = 10 // 5
txt = "x // y = {}"
print(txt.format(z))
print("\n")

print("Great! Now let's move assign different operations to x.")
print("Lets let x = 5.")
x = 5
x += 3
txt = "x += 3 = {}"
print(txt.format(x))
x -= 3
txt = "x -= 3 = {}"
print(txt.format(x))
x *= 3
txt = "x *= 3 = {}"
print(txt.format(x))
x /= 3
txt = "x /= 3 = {}"
print(txt.format(x))
x %= 3
txt = "x %= 3 = {}"
print(txt.format(x))
x **= 3
txt = "x **= 3 = {}"
print(txt.format(x))
x //= 3
txt = "x //= 3 = {}"
print(txt.format(x))
x &= 3
txt = "x &= 3 = {}"
print(txt.format(x))
x |= 3
txt = "x |= 3 = {}"
print(txt.format(x))
print("Okay, now let x = 100")
x=100
x ^= 3
txt = "x ^= 3 = {}"
print(txt.format(x))
x >>= 3
txt = "x >>= 3 = {}"
print(txt.format(x))
x <<= 3
txt = "x <<= 3 = {}"
print(txt.format(x))
print("\n")

print("Good work! Now lets use some compare operations shall we.")
print("Lets use x = 10 and y = 5 again. And T/F")
x = 10
y = 5
z = x == y
txt = "Is x equal to y? {}"
print(txt.format(z))
z = x != y
txt = "Is x NOT equal to y? {}"
print(txt.format(z))
z = x > y
txt = "Is x greater than y? {}"
print(txt.format(z))
z = x < y
txt = "Is x less than y? {}"
print(txt.format(z))
z = x >= y
txt = "Is x greater than or equal to y? {}"
print(txt.format(z))
z = x <= y
txt = "Is x less than or equal to y? {}"
print(txt.format(z))
z = (x > 3 and x < 10)
txt = "Is x greater than 3 AND less than 10? {}"
print(txt.format(z))
z = (x > 3 or x < 10)
txt = "Is x greater than 3 OR less than 10? {}"
print(txt.format(z))
z = not(x > 3 and x < 10)
txt = "Revers the result of if x greater than 3 and less than 10? {}"
print(txt.format(z))
print("\n")

print("Excellent work! These are the building blocks for more advance work.")
print("Lets continue with membership operations.")
print("Membership operations are used to test if a sequence is presented in an object.")
print("Lets let our list x be oranges and apples.")
x = ["oranges", "apples"]
print("Are oranges in list x?")
print("oranges" in x)
print("Are oranges NOT in list x?")
print("oranges" not in x)
