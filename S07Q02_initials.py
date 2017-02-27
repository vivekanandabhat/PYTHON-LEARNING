""" Get user input of his/her name in first name & last name order.
    Find the best possible initials by eliminating last character from the name
    until only one character remains in his first name or last name
"""

   

def print_name(fname, lname):
    fname_length = len(fname)
    lname_length = len(lname)

    if (fname_length > lname_length):
        fname_length=fname_length-lname_length+1
        lname_length=lname_length-lname_length+1
        print "The best possible initials are :", fname[0:fname_length], lname[0:lname_length]
    elif (fname_length < lname_length):
        fname_length=fname_length-fname_length+1
        lname_length=lname_length-fname_length+1
        print "The best possible initials are :", fname[0:fname_length], lname[0:lname_length]
    else :
        fname_length=fname_length-fname_length+1
        lname_length=lname_length-lname_length+1
        print "The best possible initials are :", fname[0:fname_length], lname[0:lname_length]

def get_name():
    """ This function fetches the name from user in first name & last name order
    """
    first=raw_input("Enter Your First name : ")
    last=raw_input("Enter your Last name : ")
    

    return first, last




# Main starts from here
first_name, last_name = get_name()
print_name(first_name, last_name)
