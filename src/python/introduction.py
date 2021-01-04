# SIMPLE MATH

# Addition
1 + 2 # = 3
2 + 4 # = 6

# Subtraction
2 - 3 # = -1
3 - 2 # = 1

# Multiplication
-1 * 2 # = -2
3 * 4 # = 12

# Division
2 / 6 # = .33333
6 / 2 # = 3

# Exponentiation (Powers)
2 ** 6 # = 64
3 ** 3 # = 27

# Integer division (Whole number division)
2 // 16 # = 0
10 // 8 # = 1

# Modulo (Remainder)
6 % 3 # = 0
7 % 3 # = 1

# COMPLEX MATH

# Import the math library
import math

# Trig functions
math.sin(math.pi) # = 0
math.cos(math.pi) # = -1
math.tan(math.pi) # = 0

# Rounding functions
math.floor(10.2) # = 10
math.ceil(10.2) # = 11

# Absolute value
math.fabs(-100) # = 100

# Factorial
math.factorial(4) # = 1 * 2 * 3 * 4 = 24

# Logarithms
math.log(4) # = ln(4) = 1.3862943611
math.log(100, 10) # = log_10(100) = 2
math.log10(100) # = log_10(100) = 2
math.log(100, 5) # = log_5(100) = 2.8613531161

# BOOLEANS AND LOGICAL OPERATIONS

# The boolean types
True
False

# Logical and
True and True # = True
True and False # = False
False and True # = False
False and False # = False

# Logical or
True or True # = True
True or False # = True
False or True # = True
False or False # = False

# Logical not
not True # = False
not False # = True

# Logical xor
True ^ True # = False
True ^ False # = True
False ^ True # = True
False ^ False # = False

# CONDITIONAL EXPRESSIONS

# Equality
1 == 2 # = False
6 == 6 # = True

6 != 9 # = True
12 != 12 # = False

# Inequality
1 > 2 # = False
6 > 6 # = False

6 >= 9 # = False
12 >= 12 # = True

6 < 9 # = True
12 < 12 # = False

1 <= 2 # = True
6 <= 6 # = True

# STRINGS

# Strings
"Strings can be defined using double quotes"
'or using single quotes'

"they're late"
'And then he said "Oh no you did not!"'

# Escaping quotes
'They\'re having a lot of fun and yelling "yippee"'
"They're having a lot of fun and yelling \"yippee\""

# String concatenation/addition
"Hello" + "world" # = "Helloworld"

# Multiline Strings
"""Hello there
this string
spans across
multiple lines :D"""

"Hello there\nthis string\nspans across\nmultiple lines :D"

# COMMENTS

# Cool single line comment

2 + 5 # Cool comment after code

"""
Weird whacky multiline string acting as a
multiline comment
"""

# Or just use
# Multiple lines of these
# Like a sane human being

# DRAWING AND IMAGES

# Importing turtle
import turtle

# Setting the turtle's color
turtle.color('red', 'yellow')

# Turtle movement
turtle.forward(10)
turtle.left(120)

# Turtle pen control
turtle.penup()
turtle.pencolor('red')
turtle.pendown()

# Turtle teleportation
turtle.setx(-100)
turtle.sety(100)

# Being done with turtles
turtle.done()
