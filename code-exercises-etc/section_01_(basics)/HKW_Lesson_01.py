##twitter = "@hearmecode"
##members = 902
##
##print twitter
##
##print "Contact Info:\n Shannon \t shannon@hearmecode.com"
##print "Contact Info:\nShannon\tshannon@hearmecode.com"
##print "Lesson\tTopic\n1\tStrings and Conditionals\n2\tLists and Loops\n3\tDictionaries & Files"
##lessonlist = "Lesson\tTopic\n1\tStrings and Conditionals\n2\tLists and Loops\n3\tDictionaries & Files"
##print lessonlist
##len(twitter)
##print len(twitter)
##name = "Hannah Kristin Warren"
####print len(name)
####print "Hannah Kristin Warren"[0]
####print name[:14]
####print name[14:]
####print name[-6:-1]
####print name[-6:]
##
##phone = "(315) 748 6402"
####print phone[:5]
####print phone[1:4]
####print phone[6:9]
##
##age = 26
##loc = "Liverpool"
##print "My name is: {0} and my age is: {1} and I live in: {2}." .format(name, age, loc)
##print "My name is: {0} and my age is: {1} and I live in: {2}." .format(name, age, loc[:4])
##print "Call {0} at {1} for more information." .format(name, phone[6:])
##
##exphone = "202-555-9876"
##print "Area Code: {0}\nLocal: {1} \nDifferent Format: ({0}) {1}".format(exphone[:3], exphone[4:])
##print exphone .find("6")
###NOTE that the following does not permanently change the variable twitter. 
##print twitter.replace("@", "#")
###this statement will permanentaly change the variable twitter. 
##twitter = twitter.replace("@", "#")
##print twitter
##length = len(twitter)

##students = 10
##capacity = 50
##teaching_assistants = 5
##
##if students < capacity:
##        print "Keep recruiting"
##elif students = capacity:
##    print "We're at capacity!" 
##else: print "End ticket signups"
##
##if teaching_assistants == 0:
##    print "None? Uh oh!"
#### think: "But! if..." i.e. this next section is only read if the first if statement is false...
##elif teaching_assistants < students/5:
##    print "Keep recruiting TA's"
#### For every other situation:
##else:
##    print "Arents the TA's great though?"

volunteers = 90
goal = 100

if volunteers < goal:
    print "We need more volunteers! We are behind."
elif volunteers == goal:
    print "You met your goal! Congratulations!"
else:
    print "No more volunteers needed."
