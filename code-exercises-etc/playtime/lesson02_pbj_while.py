# Goal #1: Write a new version of the PB&J program that uses a while loop.
#Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

slices_bread = raw_input("How many slices of bread do you have?")
peanut_butter = raw_input("How many servings of peanut butter do you have?")
jelly = raw_input("How many servings of jelly do you have?")

#convert string input variables into integers - didn't know this was a thing, thanks KristenLinkLogan! https://www.codecademy.com/forum_questions/5021453287b2ae00020082bf
slices_bread = int(slices_bread)
peanut_butter = int(peanut_butter)
jelly = int(jelly) 

sandwiches = 0

while (slices_bread >= 2) and (peanut_butter >= 1) and (jelly >= 1):
    sandwiches = sandwiches + 1
    print "Making sandwich #{0}".format(sandwiches)
    slices_bread = (slices_bread - 2)
    jelly = (jelly - 1)
    peanut_butter = (peanut_butter - 1)

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

    if peanut_butter >= 1 and slices_bread >= 2 and jelly >= 1:
        print "You have enough bread for {0} more sandwich(es), enough peanut butter for {1} more, and enough jelly for {2} more.".format(slices_bread/2, peanut_butter, jelly)
    elif peanut_butter == 0:
        print "Fini! Out of peanut butter."
    elif slices_bread <= 1:
        print "Fini! Out of bread."
    elif jelly == 0:
        print "Fini! Out of jelly."
    else:
        print "Can't make a sandwich. :("

