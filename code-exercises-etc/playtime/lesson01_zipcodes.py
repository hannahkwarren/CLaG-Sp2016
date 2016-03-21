# Challenge Level: Intermediate and Advanced

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially because you're putting them up on GitHub!

# For the purposes of this exercise, we're going to use unrealistically perfect and uniform addresses, and one-word first names :)

studybuddy_1 = 'Alison McCauley, 1234 County Line Road, Skaneateles, NY 13152'
studybuddy_2 = 'Dee Cater, 555 Bradford Pkwy, Syracuse, NY 13224'
studybuddy_3 = 'Andrea Bianchi, 987 South St, Jamesville, NY 13078'
studybuddy_4 = 'Kristen Link Logan, 264 Craig Street, Syracuse, NY 13211'
studybuddy_5 = 'Nina Verity, 111 Bridge St, Solvey, NY 13209'

# Goal 1: Create a program that simply shows all the ZIP codes.
print studybuddy_1[-5:]
print studybuddy_2[-5:]
print studybuddy_3[-5:]
print studybuddy_4[-5:]
print studybuddy_5[-5:]

# Goal 2: Modify your program to output all the ZIP codes on the same line, with an an explanatory sentence.
print "Our study group includes people from the following ZIP codes: {0}, {1}, {2}, {3}, {4}.".format(studybuddy_1[-5:], studybuddy_2[-5:], studybuddy_3[-5:], studybuddy_4[-5:], studybuddy_5[-5:])

# Goal 3: Modify your program to show each study buddy's first name and ZIP code.
buddy1_fname = studybuddy_1.find(" ")
buddy2_fname = studybuddy_2.find(" ")
buddy3_fname = studybuddy_3.find(" ")
buddy4_fname = studybuddy_4.find(" ")
buddy5_fname = studybuddy_5.find(" ")

print "{0} lives in {1}.".format(studybuddy_1[0:buddy1_fname], studybuddy_1[-5:])
print "{0} lives in {1}.".format(studybuddy_2[0:buddy2_fname], studybuddy_2[-5:])
print "{0} lives in {1}.".format(studybuddy_3[0:buddy3_fname], studybuddy_3[-5:])
print "{0} lives in {1}.".format(studybuddy_4[0:buddy4_fname], studybuddy_4[-5:])
print "{0} lives in {1}.".format(studybuddy_5[0:buddy5_fname], studybuddy_5[-5:])


