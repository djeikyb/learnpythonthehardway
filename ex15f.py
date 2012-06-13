from sys import argv

script, filename = argv

prompt = "> "
txt = open(filename)

print "Here's your file %r:" % filename
print prompt, txt.readline()
print "We're at file position: ", txt.tell()
txt.seek(10,1)
print "Now we're at: ", txt.tell()
print prompt, txt.readline()
txt.flush()
txt.seek(0,0)
print prompt, txt.read()
txt.close()

# vim: syntax=off
