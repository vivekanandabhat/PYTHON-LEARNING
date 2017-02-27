""" Get user input of his/her name in first name & last name order.
    Print user's name in the order
    - Name : First name, Surname : Last name 
    - DHARMENDER SINGH
    ------------ ------
    - Dharmender, Singh
"""


def print_name(fname, lname):
    fname_length = len(fname)
    lname_length = len(lname)
    fname_cap = fname.upper()
    lname_cap = lname.upper()
    fname_small = fname.lower()
    lname_small = lname.lower()
    print "--> Name :", fname_small, "    Surname :", lname_small
    print "-->", fname_cap, lname_cap
    print "-->", "-" * fname_length, "-" * lname_length
    print "-->", fname,",",lname
    

def get_name():
    """ This function fetches the name from user in first name & last name order
    """
    first=raw_input("Enter Your First name : ")
    
    last=raw_input("Enter your Last name : ")
    

    return first, last




# Main starts from here
first_name, last_name = get_name()
print_name(first_name, last_name)
