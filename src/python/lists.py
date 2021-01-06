# Lists

MY_FIRST_LIST = [0, 1, 2]
MY_SECOND_LIST = ["Joe", "Fred", "Hubert"]


# Getting data from a list
FRUIT_WORDS = ["apple", "bananna", "cherry"]

print(FRUIT_WORDS[0]) # Prints "apple"
print(FRUIT_WORDS[1]) # Prints "bananna"
print(FRUIT_WORDS[2]) # Prints "cherry"


# Mutating lists
fruit_words = ["apple", "bananna", "cherry"]

FRUIT_WORDS[1] = "berries" # Changes "bananna" to "berries"

print(FRUIT_WORDS[1]) # Prints "berries"


# Appending to a list
my_list = ["a", "b", "c"]
my_list.append("d")
print(my_list) # Prints "['a', 'b', 'c', 'd']"


# Removing an element from a list
my_list.remove("b")
print(my_list) # Prints "['a', 'c', 'd']"


# Get the length of a list
FRUIT_WORDS = ["apple", "bananna", "cherry"]

print(len(FRUIT_WORDS)) # Prints "3"


# Processing lists
FRUIT_WORDS = ["apple", "bananna", "cherry"]

for fruit in FRUIT_WORDS:
    print(fruit) # Will print each name in the list


# Lists and mutations

# We may want to produce a single value based on all the items
# in a list, such as a sum

# sum : ListOfNumbers -> Number
# Sums up all the numbers in a list of numbers
def sum(list_of_numbers):
    result = 0 # We start with a sum of 0

    for n in list_of_numbers: # Loop over every number `n` in the list
        result += n # Add the current number to the sum

    # Note the un-indentation, since this return is outside of the for loop
    # If the return was inside of the for loop, the function would return the
    # sum after only adding the first value, basically returning the first value
    return result # Give the result to the caller

sum([0, 2, 3, 4]) # = 9
sum([6]) # = 6
sum([15, 21, 55]) # = 91

# EXAMPLE: Counting

# count_big_strings : ListOfStrings -> Nat
# Count the number of strings that have at least 10 letters
def count_big_strings(list_of_strings):
    count = 0 # We have 0 big strings by default

    for s in list_of_strings: # Loop over every string `s` in the list
        if len(s) >= 10: # This will check if the condition is true
            count += 1 # And run this code if it is true, hence the name
    
    return count # Return the result, outside of the for and if statement