# allow us to take arguments for the script
from sys import argv

# unpack the first two argv array elements
script, filename = argv

# variable txt is now an open file
txt = open(filename)

# print the file name
print "Here's your file %r:" % filename
# read and print the open file that is txt
print txt.read()

# ask the user to painstakingly type the file name
# even though they already passed it as an argument
print "Type the filename again:"
file_again = raw_input("> ")

# variable 'txt_again' now holds an open file
txt_again = open(file_again)

# read and print the open file txt_again
print txt_again.read()

# vim: syntax=off
