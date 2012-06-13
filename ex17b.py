from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()
input.close()
output = open(to_file, 'w')
output.write(indata)
output.close()

# vim: syntax=off
