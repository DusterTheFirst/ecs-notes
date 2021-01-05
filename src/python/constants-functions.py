# Code from last class
import turtle
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.done()

# LOTS OF REPETITION ABOVE :(
# THE SIZE OF THE SQUARE AND THE ANGLE DO NOT CHANGE

# We can instead use constants
SIZE = 150
ANGLE = 90

turtle.forward(SIZE)
turtle.left(ANGLE)
turtle.forward(SIZE)
turtle.left(ANGLE)
turtle.forward(SIZE)
turtle.left(ANGLE)
turtle.forward(SIZE)
turtle.done()

# Now there is just one place to change the size and angle
# Just like in scheme, we use all caps to show that the constant will never change

# A constant with spaces in its name would look like
THIS_IS_MY_CONSTANT = "hello"

# The code above is still repetitive
# We are able to stop repeating the values, but what if we could do the same with actions
# That is where functions come in

# draw_square : Number -> Image
# Draws a square of the given size
def draw_square(size):
    turtle.forward(size)
    turtle.left(ANGLE)
    turtle.forward(size)
    turtle.left(ANGLE)
    turtle.forward(size)
    turtle.left(ANGLE)
    turtle.forward(size)

# Python is a whitespace language. The content of the function needs to be
# indented or else python will not think it is coe for the function

# To use our functions, we can now call our function
draw_square(150)
draw_square(300)
turtle.done()

# We still need to write the function signature and the purpose of the function
# But tests are a bit harder to do in python than in scheme, so we will hold off on writing them for now
# To "test" your function, you can just run it a few times and analyze the result

# layout of the function
def # Tells python about the function definition
draw_square # The name of our function
(size) # Tells python that our function takes in one input, and we name it size
: # Tells python that everything after this is the content of the function

# If we were to take in 2 inputs, we would put a comma between them
def two_inputs(a, b):

# DESIGNING A FUNCTION

# Design a square root function

# square_root : Number -> Number
# Find the square root of a Number
def square_root(n):
    return n**(1/2) # n^.5 = sqrt(n)

square_root(100) # = 10.0
x = square_root(25) # = 5.0

# PRINTING VALUES

# in order to show values on the right side, we need to use the print function
print("hello")
print("hello", 7, False, 32)
print(square_root(100))

# Watch out! In python 2, the previous version of python, you can write print
# without parenthesis around the inputs. THAT WILL NOT WORK IN PYTHON 3 which is the version we use

# RETURNING NOTHING

# print_greeting : String -> (void)
# Prints a greeting to the given person
def print_greeting(name):
    print("Hello " + name)

print_greeting("Alice") # prints "Hello Alice"

# Since it returns nothing, we cannot get a value from it
greeting = print_greeting("Alice")
print(greeting) # prints "None"

# Watch out! If you do not give enough arguments to a function, repl.it
# will not give an error, but there will be an error when you run the code

# If we want to instead return and use the greeting instead of printing it
# our function would look something like

# get_greeting : String -> String
# Get a greeting to the given person
def get_greeting(name):
    return "Hello " + name

get_greeting("Alice") # = "Hello Alice"

# Since it returns something, we can now get a value from it
greeting = get_greeting("Alice")
print(greeting + "'s dog") # prints "Hello Alice's dog"

# MUTATION

# What would this code do?
x = 7
x = 10
print(x)

# THe changing of values is called mutation

# Answer: The first line will define x as 7
# and then the second line will change x to 10
# so print(x) will print 10

# Changing the value relatively

# Sometimes we want to change the value like
x = x + 3
# which would add 3 to value stored in x and then store it in x

# python gives us a tool to do this using +=
x += 3
# adds 3 to the value stored in x in place

# We can do this with all the mathematical operators
x -= 3 # subtracts 3 from the value x
x *= 3 # multiplies 3 to the value x
x /= 3 # divides 3 from the value x

# Weirdly, we can use these with strings too
s = "Hello"
s += "!" # Adds a "!" at the end of the string s
s *= 3 # Duplicates the string s 3 times
print(s) # prints "Hello!Hello!Hello!"

# MUTATION WEIRDNESS

# mutating an input to a function is whacky

# Say we have this function

# change_number : Number -> (void)
# Add 3 to the given Number
def change_number(x):
    x += 3

# And this code that calls the function
x = 10
change_number(x)
print(x)

# That print at the end would print 10, but shouldn't it print
# 13?

# NO cause they are not the same, they just have the same value

# if we want to mutate or change values passed to us, we need to return
# them with their new values out of the function so that they can be used

# change_number : Number -> Number
# Add 3 to the given Number
def change_number(x):
    x += 3
    return x

# and then to use the function, we would do
x = 10
x = change_number(x) # Move the changed value of x into x so we can use it
print(x)

# EXERCISES

# GIVEN
def change1(x):
    x += 3
    return x

def change2(a):
    a -= 5
    return a

def change3(s):
    s *= 2

# ACTIONS
a = 7
b = "hello"
c = 10

b = change1(a)
change3(b)
c = change2(c)

print(a, b, c)

# Answer: a: 7, b: 10, c: 5

a = 7
b = "hello"
c = 10

b = change1(a) # = a + 3
change3(b) # NO CHANGE
c = change2(c) # = c - 5

# a: UNCHANGED  = 7
# b: a + 3      = 10
# c: c - 5      = 5
print(a, b, c)