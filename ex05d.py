name = 'Zed A. Shaw'
age = 35 # not a lie
height_in = 74
height_cm = height_in * 2.54
weight_lb = 180
weight_kg = weight_lb * 0.4536
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %d inches tall." % height_in
print "He's %d centimetres tall." % height_cm
print "He's %d pounds heavy." % weight_lb
print "He's %d kilos heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %r." % (
    age, height_in, weight_lb, age + height_in + weight_lb)

# http://docs.python.org/library/stdtypes.html

# vim: syntax=off
