""" Get user input of a long sentence.
    Find the last character; last 5 characters.
    characters between 2 and 5 position
    character at centre and its adjoining characters.
"""

def middle_sent(sent,mid):
    print "The character at the centre of sentence is :", sent[mid-1]
    print "The centre 3 characters of the sentence are :", sent[mid-2 : mid+1]

def find_char(sentenc):
    length=len(sentenc)
    print "The total characters in the sentence entered is :", length
    print "The last character of the entered sentence is :", sentenc[-1]
    print "The last 5 characters of the sentence is :", sentenc[-5:]
    print "The characters between 2 and 5 positions in the sentence is :", sentenc[3:5]
    print "The characters at 2nd and 5th position of the sentence is :", sentenc[2], sentenc[5]

    if (length%2 == 0):
        middle = length /2     
    else :
        middle = (length / 2) + 1
        
    middle_sent(sentenc,middle)


def get_name():
    """ This function fetches thesentence from user
    """
    sent=raw_input("Enter a long sentence of your choice : ")
    return sent
   

# Main starts from here
sentence = get_name()
find_char(sentence)
