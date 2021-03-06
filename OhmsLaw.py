"""
This program prompts the user to enter voltage (in Volts)
and resistance (in Ohms) to output current (in Amps).
Code based off CS-161 Programming Assignment (Jesse Black)
Sources: phet.colorodor.edu/simus/html/ohms-law
"""

print("This program allows the user to enter voltage in volts, and resistance in Ohm.")
print("Then tells the user the current in Amps.")

voltage = raw_input("Enter voltage in Volts: ")
resistance = raw_input("Enter resistance in Ohms: ")

v = float(voltage)
r = float(resistance)

current = v/r

txt = "The current is Amps is {}"
print(txt.format(current))
