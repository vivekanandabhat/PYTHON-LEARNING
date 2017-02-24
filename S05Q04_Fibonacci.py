"""  Take a number as input from the user. 
     Find which Fibonacci number is nearest to that number and print it.
"""



def print_near_fibo(num) :

    a = 1
    b = 1
    c = 2

    while (c < num) :
        a = b
        b = c
        c = a + b

    if (( c - num ) > ( num - b )) :
        print "The nearest fibonacci number to ", num, "is :", b
    else :
        print "The nearest fibonacci number to ", num, "is :", c
        


        

def get_number():
    """ This function prompts the user for a number
        It returns an integer.
    """
    num = raw_input("Enter the number of your choice : ")
    return int(num)


# Main starts from here
number = get_number()
print_near_fibo(number)
