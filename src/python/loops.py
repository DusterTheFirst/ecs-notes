# for loops using range()

# fibinnaci

# for loops over strings

for letter in "aahhhhhh":
    print(letter) # Will print out each character individually


# Example

# separate_by_space : String -> ListOfStrings
# Separate the given text by spaces
# ex: separate_by_space("a b c") -> ["a", "b", "c"]
def separate_by_space(string):
    result = [] # We always need a result that we accumulate the values int
                # it always needs to have a default value that we would expect
                # If the loop runs 0 time

    current_word = "" # For loops only give us information about the current
                      # characters we need to store the seen characters in here

    for letter in string:
        if letter == " ": # If the letter we see is a space, add the word to the result
            result.append(current_word)
            current_word = "" # And reset the current word to empty
        else:
            current_word += letter # If not a space, add the character to the current_word
    
    result.append(current_word) # Add the last word to the list

    return result


# While loops

num = 1
while num < 6: # While will run the code in its loop until this conditional becomes
               # False
    print(num)
    num += 1

# The above code will print out 1, 2, 3, 4, 5


# While loops are useful when you do not know how much the loop needs to run

# find_perfect_square : Number -> Number
# Returns the first perfect square larger than the given number
# find_perfect_square(6) -> 9
# find_perfect_square(90) -> 100
def find_perfect_square(starting_number):
    while not perfect_square(starting_number):
        starting_number += 1
    return starting_number

# perfect_square : Number -> Boolean
# Is this a perfect square?
def perfect_square(n):
    return n ** (1/2) % 1 == 0 # sqrt(n) and then get the remainder, making sure it is 0


# collatz conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture)
# if you have an even number, divide by 2
# if you have an odd number, multiply by 3 and add 1

# ie 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# collatz: Number -> Nat
# Returns the number of steps it took to get from the given number to 1
def collatz(n):
    steps = 0 # Place to store the amount of steps we did

    while n > 1: # Make sure n is > 1
        steps += 1 # Increment the step count for each loop
        if n % 2 == 0: # Check if n is even
            n /= 2 # divide by 2
        else:
            n = n * 3 + 1 # multiply by 3 and add 1
    
    return steps

# Nesting loops
for x in range(3):
    y = x
    while y >= 0:
        print(x, y)
        y -= 1

# Prints
# 0 0
# 1 1
# 1 0
# 2 2
# 2 1
# 2 0

# Note how the numbers count up in both the x and y column

for x in range(3):
    for y in range(3):
        print(x, y)

# Prints
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# Stopping loops

for num in range(10):
    if num % 3 == 0:
        break

    print(num)

# This loop will count 1 2
# but since the number 3 is divisible by 3 evenly, it will "break" out of the loop
# and stop the loop fom running early

# Sometimes you don't want to break the loop, but just skip a step

for num in range(10):
    if num % 3 == 0:
        continue

    print(num)

# This loop will count 1 2 4 5 7 8
# for all numbers divisible by 3, it will skip the 3