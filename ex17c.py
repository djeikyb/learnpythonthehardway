# see how short can make it

from sys import argv

open(argv[2], 'w').write(open(argv[1]).read())

# vim: syntax=off
