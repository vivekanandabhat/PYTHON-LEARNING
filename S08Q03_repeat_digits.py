""" Get user to input a number.
     If the user enters a number as 5, then
     generate the following string :
     - 00001111222233334444
     - If the user enters the number as 3, then
     generate the following string :
     - 001122
"""


def digit(number):
    list_num = []
    for item in range(0, number):
        add = str(item) * (number-1)
        list_num.append(add)

    list_num = "".join(list_num)
    print list_num
        

def get_name():
    """ This function fetches a number from user
    """
    num=raw_input("Enter a number of your choice : ")
    return int(num)

# Main starts from here
number = get_name()
digit(number)
