# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
peanutb = 1
jelly = 1
bread = 1

if (peanutb > 0) and (jelly > 0) and (bread >= 2):
	print "You can make a sandwich! Enjoy!"
elif bread == 1:
	print "You can't make a full sandwich. Halfsies. :("
else: print "No pb&j for you. Boo."

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make
peanutb = 1
jelly = 1
bread = 8
full_sandwiches = (bread / 2)

if (peanutb > 0) and (jelly > 0) and (full_sandwiches >= 1):
    print "Based on how much bread you have, you can make {2} sandwiches!".format(peanutb, jelly, full_sandwiches) 
else: print "You can't make any sandwiches. :("

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )
peanutb = 1
jelly = 1
bread = 8
full_sandwiches = (bread / 2)
if ((bread % 2) == 1):
        print "Based on how much bread you have, you can make {0} full sandwiches and 1 open-faced sandwich - or, you could just make {1} open-faced sandwiche(s).".format(full_sandwiches, bread) 

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches.
peanutb = 0
jelly = 0
bread = 0
full_sandwiches = (bread / 2)

if (peanutb > 0) and (jelly > 0) and (bread >= 2):
	print "You can make a sandwich! Enjoy!"
elif bread == 1:
	print "You can't make a full sandwich. Halfsies. :("
else: print "No pb&j for you. Boo."

if (full_sandwiches >= 1) and (bread == 0) and (jelly == 0): print "You can\'t make anything involving peanut butter, jelly, or bread. Try pasta instead!"
elif (peanutb == 0) and (jelly == 0): print "You need peanut butter and jelly! Maybe make a different kind of sandwich."
elif (jelly == 0) and (full_sandwiches >= 1): print "You can't make a sandwich at all - no bread or jelly! Maybe put peanut butter on a cracker...?"
elif (peanutb == 0) and (full_sandwiches >= 1): print "You can't make a sandwich. Jelly isn't any good without bread, and you need bread and peanut butter!"
elif peanutb == 0: print "You are out of peanut butter! You need to buy some before you can make a sandwich."
elif jelly == 0: print "You are out of jelly! You need to buy some before you can make a sandwich."
elif (full_sandwiches == 0): print "You are out of bread! You need to buy some before you can make a sandwich... or use crackers!"
else: print "You're in business; you can make some kind of pb&j."    

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.
if (peanutb > 0) and (jelly > 0) and (bread >= 2):
	print "You can make a sandwich! Enjoy!"
elif (peanutb > 0) and (bread >= 2) and (jelly == 0):
    print "You don't have jelly, but you can make a plain peanut butter sandwich."

