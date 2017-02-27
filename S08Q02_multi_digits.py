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


def do_digit_oper(no,l) :
    if (l==1):
        no = no + 7
        print " The number after adding seven to it is :", no
        unit_place(no)
    elif (l==2):
        no = no**5
        print " The number after raising to the power of 5 is :", no
        unit_place(no)
    else :
        new_num = raw_input("Enter another number of your choice : ")
        new_num = int(new_num)

        no = no + new_num
        print "The number after adding the 2 inputs is :", no
        unit_place(no)
        
     
    
def check_digit(number, lenth) :
    """ This function uses helper functions
        Checks for greater than 3 digit number & prints appropriate o/p.
        Also, calls appropriate helper function if number is within 3 digits.
    """

    if (lenth >=4) :
        print "You have entered a number greater than 3 digits. Invalid input for this example."
    else :
        do_digit_oper(number,lenth)  
    
   
def get_number():
    """ This function prompts the user for a number
        It returns an integer.
    """
    number = raw_input("Enter any non negative number of your choice : ")
    lnth=len(number)
    return lnth, int(number)
    
    
# Main starts from here
length, num = get_number()
check_digit(num,length)


