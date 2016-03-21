# Can you make Python print out the song for 99 bottles of beer on the wall?
# Helpful mnemonic: range(start, stop, step)

for bottles in range(99, 1, -1):
    print "({0} bottles of beer on the wall, {0} bottles of beer...".format(bottles)
    print "Take one down, toss it around, {0} bottles of beer on the wall!".format(bottles - 1)

#Stolen from KristenLinkLogan
print "2 bottles of beer on the wall, 2 bottles of beer..."
print "Take one down, toss it around, 1 bottle of beer on the wall!"
