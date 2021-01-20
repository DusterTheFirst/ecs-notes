# Opening files
open("testing.txt", "r") # Read to file
open("testing.txt", "w") # Write to file
open("testing.txt", "a") # Append (read what is in the file, and add some more)
open("testing.txt", "r+") # Read and write

# Reading a file
f = open("testing.txt", "r")
file_contents = f.read() # Reads in all the content from the file

# Reading each line
f = open("testing.txt", "r")
line1 = f.readline() # Reads in the first line
line2 = f.readline() # Reads in the second line

entire_contents = f.read() # This will read in everything past the
                           # first two lines, since f.readline() eats
                           # up the line when it reads it. We can no
                           # longer read that part of the file

# Reading all lines
f = open("testing.txt", "r")
all_lines = f.readlines() # Returns a list of all the lines
all_lines = list(f) # Same as above


# Reading each line in a file
f = open("testing.txt", "r")

for line in f:
    print(line)
