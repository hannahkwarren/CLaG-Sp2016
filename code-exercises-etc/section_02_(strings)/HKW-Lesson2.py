##attendees = ['Hannah', 'Kseniya', 'Sarah', 'Christy']
##print [0]
##print [1]
##print [2]
##
##number_of_attendees = len(attendees)
##print number_of_attendees
##
###append, add one item at a time to the end of the list
##attendees.append ('Alison')
##print attendees
##
##attendees_ages = []
##attendees_ages.append(29)
##attendees_ages.append(33)
##print attendees_ages
##
##attendees_ages[0] = 30
##print attendees_ages
##
##days_week = ['Monday','Tuesday']
##days_week.append('Wednesday')
##days_week.append('Thursday')
##days_week.append('Friday')
##days_week.append('Saturday')
##days_week.append('Sunday')
##print days_week
##print len(days_week)
##
###.pop by default removes last item in list
##days_week.pop() #or days_week.pop(), same thing without index
##
##print days_week
##print len(days_week)
##
##day = days_week.pop(3)
##print day
##
##print "\nHere is the months exercise:"
##months = ['January','February']
##month3 = 'March'
##months.append(month3)
##months.extend(['April','May','June','July','August','September','October','November','December'])
##months.insert (0, 'New 1st month of the year!')
##print months.pop(12)
##print months
##
###split exercise
##print "Here is the split example - making an address into a list, separating at each space."
##address = "1133 19th St NW Washington, DC 20036"
##address_as_list = address.split(" ")
##print address_as_list
##
###in keyword allows checking whether a value exists in the list
##print 'ann' in 'Shannon'
##name = 'Shannon'
##print 'ann' in name
##if 'Wednesday' in days_week:
##    print "Wednesday is a day of the week!"
##print 'Frankenstein' in address
##
##print "Hello there, {0}!".format(raw_input('Enter your name.'))
##attendees = []
##attendee1_name = raw_input('Provide the first attendee name.')
##print attendee1_name
##attendees.append(attendee1_name)
##print attendees
##print len(attendees)

##print "Hello there, {0}! Please enter an address.".format(raw_input('Enter your name.'))
##
##addresses = []
##addressesNW = []
##addressesNE = []
##addressesSE = []
##addressesSW = []
##
##address1 = raw_input('Provide the first address.')
##
##addresses.append(address1)
##if ' NW ' in address1 or ' nw ' in address1:
##    addressesNW.append(address1)
##elif ' NE ' in address1 or ' ne ' in address1:
##    addressesNE.append(address1)
##elif ' SE ' in address1 or ' se ' in address1:
##    addressesSE.append(address1)
##elif ' SW ' in address1 or 'sw ' in address1:
##    addressesSW.append(address1)
##else:
##    print "Your address is not located in a quadrant in Washington, DC."
##
##address2 = raw_input('Provide the second address.')
##
##addresses.append(address2)
##if ' NW ' in address2 or ' nw ' in address2:
##    addressesNW.append(address2)
##elif ' NE ' in address2 or ' ne ' in address2:
##    addressesNE.append(address2)
##elif ' SE ' in address2 or ' se ' in address2:
##    addressesSE.append(address2)
##elif ' SW ' in address2 or ' sw ' in address2:
##    addressesSW.append(address2)
##else:
##    print "Your address is not located in a quadrant in Washington, DC."
##
##address3 = raw_input('Provide the third address.')
##if ' NW ' in address3 or ' nw ' in address3:
##    addressesNW.append(address3)
##elif ' NE ' in address3 or ' ne ' in address3:
##    addressesNE.append(address3)
##elif ' SE ' in address3 or ' se ' in address3:
##    addressesSE.append(address3)
##elif ' SW ' in address3 or ' sw ' in address3:
##    addressesSW.append(address3)
##else:
##    print "Your address is not located in a quadrant in Washington, DC."
##
##print "There are {0} addresses in the list \"addressesNW.\" They are: {1}.".format(len(addressesNW), addressesNW)
##print "There are {0} addresses in the list \"addressesNE.\" They are: {1}.".format(len(addressesNE), addressesNE)
##print "There are {0} addresses in the list \"addressesSE.\" They are: {1}.".format(len(addressesSE), addressesSE)
##print "There are {0} addresses in the list \"addressesSW.\" They are: {1}.".format(len(addressesSW), addressesSW)
##print len(addresses) 
##
###loops iterate through lists... for variable in range, "variable" is a local variable, set at each iteration in a loop
##print range(10)
##my_list = range(10)
##for cow in range(10):
##    #cow = first iten in the list you're asking me to iterate through... which is 0
##    #print that first
##    print cow

print "Hello there, {0}! Please enter an address.".format(raw_input('Enter your name.'))

addresses = []
addressesNW = []
addressesNE = []
addressesSE = []
addressesSW = []

for address in range(3):
    address = raw_input('Provide the first address.')

addresses.append(address)
if ' NW ' in address or ' nw ' in address:
    addressesNW.append(address1)
elif ' NE ' in address or ' ne ' in address:
    addressesNE.append(address1)
elif ' SE ' in address or ' se ' in address:
    addressesSE.append(address1)
elif ' SW ' in address or 'sw ' in address:
    addressesSW.append(address1)
else:
    print "Your address is not located in a quadrant in Washington, DC."

print "There are {0} addresses in the list \"addressesNW.\" They are: {1}.".format(len(addressesNW), addressesNW)
print "There are {0} addresses in the list \"addressesNE.\" They are: {1}.".format(len(addressesNE), addressesNE)
print "There are {0} addresses in the list \"addressesSE.\" They are: {1}.".format(len(addressesSE), addressesSE)
print "There are {0} addresses in the list \"addressesSW.\" They are: {1}.".format(len(addressesSW), addressesSW)
print "There are {0} addresses in the list \"addresses.\"".format(len(addresses))

for month in months_in_year:
    print month
    for week in range(1, 5):
        print "Week {0}".format(week)
        for day in days_of_week:
            print day

#enumerate
twitter_handle = ['@one','@two','@three']
for index, handle in enumerate(twitter_handle):
    print index
    print handle
    at_sign_index = handle.find('@')
    twitter_handles[index] = handle[at_sign_index + 1:]

#zip allows you to do a for loop to use each item in mutiple lists all at once; stops when it runs out of matches




