# Make variable with string, format 10 as a decimal
x = "There are %d types of people." % 10
# Make var hold string
binary = "binary"
# Make var hold string
do_not = "don't"
# Make var hold string, and insert two string holding vars
y = "Those who know %s and those who %s." % (binary, do_not)

# output
print x
# output
print y

# output a string, insert x's string
print "I said: %r." % x
# output a string, insert y's string
print "I also said: '%s'." % y
# unsure why insertion is quoted in output
# unsure why %r vs %s, no apparent difference here

# Not a string
hilarious = False
# Make var hold string
joke_evaluation = "Isn't that joke so funny?! %r"

# output
print joke_evaluation % hilarious

# Var with string
w = "This is the left side of..."
# Var with string
e = "a string with a right side."

# Output two vars holding strings
print w + e


# vim: syntax=off
