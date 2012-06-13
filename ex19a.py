# write a comment above each line explaining

# define a function. eats counters for cheese and cracker boxen
#                    shits print statements
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print var as decimal
    print "You have %d cheeses!" % cheese_count
    # print var as decimal
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # print string
    print "Man that's enough for a party!"
    # print string
    print "Get a blanket.\n"


# print string
print "We can just give the function numbers directly:"
# call function passing two decimals
cheese_and_crackers(20, 30)


# print string
print "OR, we can use variables from our script:"
# set cheese counter
amount_of_cheese = 10
# set cracker boxen counter
amount_of_crackers = 50

# call function passing cheese and cracker boxen count variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# print string
print "We can even do math inside too:"
# call function, passing two arguments. each argument uses elementary math
cheese_and_crackers(10 + 20, 5 + 60)


# print string
print "And we can combine the two, variables and math:"
# call function. each argument uses elementary algebra
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# vim: syntax=off
