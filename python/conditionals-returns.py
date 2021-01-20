# print_if_big : Number -> (void)
# Print a message if the number is big
def print_if_big(n):
    if n > 100:
        print("Wow that's a big number")

print_if_big(1000000) # prints "Wow that's a big number"
print_if_big(3) # prints nothing

# The above if *statement* can not have an else path.
# If there is no else path, it will just do nothing.

# If we were to return data from this, you might think we could write

# tell_me_if_big : Number -> String
# Return a message if the number is big
def tell_me_if_big(n):
    if n > 100:
        return "Wow that's a big number"

# This technically is not correct since only if n is > 100 will the string be returned,
# to make it correct, we would need to add an else path

# tell_me_if_big : Number -> String
# Return a message if the number is big
def tell_me_if_big(n):
    if n > 100:
        return "Wow that's a big number"
    else:
        return "Nope."

# Now that has all of the code paths return a string, and now it is correct

# PRACTICE PROBLEM

# What is printed by the following code?

MY_NAME = "MacKenzie"
courses = 5
STUDENTS = 100
if len(MY_NAME) < 10:
    print("Short name!")
if courses < 5:
    courses += 1
else:
    if STUDENTS > 50:
        print("Lots of students")
print(str(courses) + "courses")

# "MacKenzie"'s length is less than 10, so "Short name!" will be printed
# courses is = 5, so the else will be run
# the STUDENTS is > 50, so "Lots of students" will be printed
# And then the last print will always print since it is outside of any conditional
# and it will print "5courses"

# summarize : String Number Number -> String???
# Summarize the information given
def summarize(lastname, courses, students):
    if len(MY_NAME) < 10:
        return "Short name!"
    if courses < 5:
        courses += 1
    else:
        if STUDENTS > 50:
            return "Lots of students"
    print(str(courses) + "courses")

print(summarize("MacKenzie", 3, 100)) # Will print "Short name!"

# The code stopped running in the function after the return. Returns "break" out
# of the function that called them. Keep that in mind.

# But the function above does not always return, that is why the return type is a
# "String???". It is kinda wonky, so you should almost never write a function like it


# categorize : Number -> (void)
# Categorize the given number
def categorize(num):
    if num < 0:
        print("neg")
    elif num > 0:
        print("pos")
    else:
        print("zero")

# In the above function, we have 3 cases, The number being neg(ative) pos(itive)
# or zero. Since we only want one of them to run, we use if else and the new keyword
# elif.

# Elif is a shortening of else if, basically the same as we did in the previous function
# with the code
    else:
        if STUDENTS > 50:
            return "Lots of students"