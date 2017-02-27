""" Get user input of a sentence.
    Get user input for word to be replaced
    Get user input for the word that has to replace earlier word. 
"""

def find_replace(sentenc):
    """ This function fetches the word for replace & the word that replaces.
        Uses built-in function to search & replace
    """
    search=raw_input("Enter the word to be searched :")
    replace=raw_input("Give the word for replacing the above word :") 
    print sentenc.replace(search, replace)
    


def get_name():
    """ This function fetches the sentence from user.
    """
    sent=raw_input("Enter a long sentence of your choice : ")
    return sent
   

# Main starts from here
sentence = get_name()
find_replace(sentence)
