# User input
input("Enter a number: ") # Prints "Enter a number: " and waits for user input

# You can save the input in a variable
number = input("Enter a number: ")
print(number + 7) # This does not work, since input returns a string

# We can get around that with the int or float methods

# Will work with whole numbers
number = int(input("Enter a number: "))
print(number + 7)

# Will work with whole numbers and decimal numbers
number = float(input("Enter a number: "))
print(number + 7)

# > The int() and float() methods convert from a string to whole numbers
# > and decimal numbers respectively


# Randomness
import random # You need this module for randomness

print(random.randint(1, 10)) # prints a random integer from 1 to 10 inclusive

print(random.choice(["apple", "banana", "cherry"])) # prints a random element from that list

