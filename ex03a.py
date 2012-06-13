print "I will now count my chickens:"

print "Hens", 25 + 30 / 6 # (/ 30 6), (+ 25 5), 30
print "Roosters", 100 - 25 * 3 % 4 # (* 25 3), (% 75 4), (- 100 3), 97
                                   # modulo % returns the remainder

print "How I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 # (- (+ 3 2 1 6 (% 4 2)) 5 (/ 1 4))
                                        # (/ 1 4) is 0, cause no float

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7 # math, then print the boolean result of comparison
                    # < > are boolean things, not making things

print "What is 3 + 2?", 3 + 2 # print quoted stuff, print math result
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

# vim: syntax=off
