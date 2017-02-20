""" Reads user input on storage level value.
    If storage level exceeds 80% capacity, Raise alarm to close valve.
    If storage level goes less than 20% capacity, send SMS to buy more.
"""

def do_action(limit, present, redmark, bluemark):

    if (present >limit) :
        print "Ethanol Spillage; Raise alarm; Emergency procedure; Please evacuate the premises"
    elif (present >=bluemark and present <=redmark) :
        print "No problem with the current level of Ethanol storage."
    elif (present >redmark) :
        print "Storage Level is High; Raise an alarm!!! Operator.. Please close the Valve!"
    else :
        print "Storage Level has gone lower; Please send SMS to buy more Ethanol."
        


def get_current_level():

    cur_level = raw_input("What is the current level of Ethanol available in the storage tank : ")
    return int(cur_level)


# Main starts from here
capacity = 900
high = 900*80/100 
low = 900*20/100
level = get_current_level()
do_action(capacity, level, high, low)

