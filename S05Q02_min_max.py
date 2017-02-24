""" Keep getting user input until 0 is entered.
    Among all the entered numbers, find the least & max number.
    Also, find the number of 1, 2 & 3 digit numbers entered.
"""

       
def get_number():
    """ This function fetches the number from user until 0 is entered
    """
    number = 1
    mini = 100
    maxi = 0
    single = 0
    double = 0
    triple = 0
    while (number != 0):
        number=raw_input("Enter any number : ")
        number=int(number)
        if number == 0 :
            print "You have entered zero now; The details are given below :"
            break
        if (mini > number) :
            mini = number
        elif (maxi < number) :
            maxi = number
        if (number <=9) :
            single+=1
        elif (number >=10 and number <=99) :
            double+=1
        elif (number >=100 and number <=999):
            triple+=1


    print "The least number entered is : ", mini
    print "The highest number entered is : ", maxi
    print "The number of single digit numbers entered is :", single
    print "The number of double digit numbers entered is :", double
    print "The number of triple digit numbers entered is :", triple

   
# Main starts from here
get_number()




    
