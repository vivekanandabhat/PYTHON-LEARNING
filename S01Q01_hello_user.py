""" Code to get user name and wish him Hello 
"""


def get_username():
    """ Function defined to prompt user to enter his/her name ?
    """
    user=raw_input("Please enter your name : ")
    return user

def say_hello(user):
    print "Hello", user,"!!!"

# Main starts from below
name = get_username()
say_hello(name)
