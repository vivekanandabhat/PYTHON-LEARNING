""" Program takes input from user.
    1 digit==> Add 7 to that num & print the number in unit place
    2 digit ==> Get the new number which is raised to 5 of the 2 digit number
    and print the number in unit place
    3 digit ==> Get another number from user, add the two & print the number in unit's place.
"""

# Implement the helper functions here

def unit_place(numbr) :

    num_at_unit = numbr % 10
    print " The number at unit's place after the calculation is :", num_at_unit


def do_1digit_oper(no) :

    no = no + 7
    print " The number after adding seven to it is :", no
    unit_place(no)
        
     
def do_2digit_oper(no) :

    no = no**5
    print " The number after raising to the power of 5 is :", no
    unit_place(no)


def do_3digit_oper(no) :

    new_num = raw_input("Enter another number of your choice : ")
    new_num = int(new_num)

    no = no + new_num
    print "The number after adding the 2 inputs is :", no
    unit_place(no)


def check_digit(number) :
    """ This function uses helper functions
        Checks for 1, 2, 3 or any other digit and calls the appropriate helper functions
        to perform the required operations
    """

    if (number <=9) :
        do_1digit_oper(number)
    elif (number >=10 and number <=99) :
        do_2digit_oper(number)
    elif (number >=100 and number <=999) :
        do_3digit_oper(number)
    else :
        print "You have entered a 4 digit number. Invalid input for this example."
    
   
def get_number():
    """ This function prompts the user for a number
        It returns an integer.
    """
    number = raw_input("Enter any non negative number of your choice : ")
    return int(number)
    
    
# Main starts from here
num = get_number()
check_digit(num)


