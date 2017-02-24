"""  Take a number as input from the user. 
     Print the squares of numbers from 1 till the square value doesn't
     exceed the number provided by user
"""



def print_square(numbr) :

    mult = 1
    sq = 1
    while (sq < numbr) : 
        sq = mult * mult
        if (sq > numbr) :
            continue
        else :        
            print "Square of number", mult, "is", sq
            mult+=1
        

def get_number():
    """ This function prompts the user for a number
        It returns an integer.
    """
    num = raw_input("Enter the number of your choice : ")
    return int(num)


# Main starts from here
number = get_number()
print_square(number)
