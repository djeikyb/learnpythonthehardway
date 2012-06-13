from sys import argv

script, filename = argv

print """
We're going to erase %r.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
""" % filename

#raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n" + raw_input("line 4: ") + "\n")

print "And finally, we close it."
target.close()

print "Now read it."
target = open(filename, 'r')
print target.read()
target.close()

# vim: syntax=off
