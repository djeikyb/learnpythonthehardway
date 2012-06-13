from sys import argv

print "What file can I read?"
filename = raw_input("> ")

txt = open(filename)

print txt.read()

# vim: syntax=off
