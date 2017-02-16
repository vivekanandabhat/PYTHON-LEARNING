""" To Print multiplication table of a number which the user provides.
"""

def get_number():
    """ This function fetches the number from user
        This function also fetches the number upto which the table has to be printed
    """
    number=raw_input("Enter the number for which multiplication table needs to be printed : ")
    number=int(number)

    multiplier=raw_input("Enter the number upto which the multiplication table has to be printed : ")
    multiplier=int(multiplier)

    return number,multiplier


def print_mtable(no, X):
    """ This function prints the multiplication table of num
    """
    for value in range(0, X+1):
        print no, "X", value, "=", no*value
        
   
# Main starts from here
num,mult = get_number()
print_mtable(num,mult)



    
