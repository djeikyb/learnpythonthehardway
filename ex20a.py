# import argv function from sys module
from sys import argv

# assign parts of argv array to variables
script, input_file = argv

# function to read print a file to screen
def print_all(f):
    print f.read()

# function to seek to beginning of file
def rewind(f):
    f.seek(0)

# eats number, file; shits number, line of file
def print_a_line(line_count, f):
    print line_count, f.readline()

# open a file into a variable
current_file = open(input_file)

# print stuff
print "First let's print the whole file:\n"

# call function passing the current file
print_all(current_file)

# print stuff
print "Now let's rewind, kind of like a tape."

# call rewind function passing the current file
rewind(current_file)

# print stuff
print "Let's print three lines:"

# set variable to an integer
current_line = 1
# call function passing an integer and the current file
print_a_line(current_line, current_file)

# set variable to itself, plus one
current_line = current_line + 1
# call function passing an integer and the current file
print_a_line(current_line, current_file)

# set variable to itself, plus one
current_line = current_line + 1
# call function passing an integer and the current file
print_a_line(current_line, current_file)


# vim: syntax=off
