""" Program takes 2 numbers from the user & decides whether numbers entered are 2, 3 or some other digits.
"""

def perform_check(number1, number2):
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    print "The user provided numbers are :", number1, "and", number2
    
    if (number1 >=100 and number1 <=999) :
        print "The 1st number entered by you,", number1, ",is a 3 digit number."
    elif (number1 >=10 and number1 <=99) :
        print "The 1st number entered by you,", number1, ",is a 2 digit number."
    else :
        print "The 1st number entered by you,", number1, ",is neither a 2 digit nor a 3 digit number"


    if (number2 >=100 and number2 <=999) :
        print "The 2nd number entered by you,", number2, ",is a 3 digit number."
    elif (number2 >=10 and number2 <=99) :
        print "The 2nd number entered by you,", number2, ",is a 2 digit number."
    else :
        print "The 2nd number entered by you,", number2, ",is neither a 2 digit nor a 3 digit number"
            
            
def get_number():
    """ This function prompts the user for a number
        It returns an integer.
    """
    first_num = raw_input("Enter the first number of your choice : ")
    second_num = raw_input("Enter the second number of your choice : ")
    return int(first_num), int(second_num)
    
    
# Main starts from here
num1, num2 = get_number()
perform_check(num1, num2)

