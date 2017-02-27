""" Get user to input a number.
     Find the number of digits in that number
"""


def digit(number):
    length = len(number)
    print "The number of digits in", number, "is :", length
    

def get_name():
    """ This function fetches a number from user
    """
    num=raw_input("Enter a number of your choice : ")
    return num

# Main starts from here
number = get_name()
digit(number)
