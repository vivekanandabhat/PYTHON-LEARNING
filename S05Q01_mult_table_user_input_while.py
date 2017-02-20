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


def print_mtable(number, multiplier):
    """ This function prints the multiplication table of the number provided
        by the user upto the multiple which the user wants
    """
    multi = 0
    while (multi <= multiplier):
        print number, "X", multi, "=", number*multi
        multi+=1
        
   
# Main starts from here
num,mult = get_number()
print_mtable(num,mult)



    
