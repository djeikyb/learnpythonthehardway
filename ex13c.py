from sys import argv

script, one = argv

#print "Tell me about your %s." % one, raw_input()

answer = raw_input("Tell me about your %s.\n> " % argv[1])
print "%s. That's a nice %s." % (answer, argv[1])

# vim: syntax=off
