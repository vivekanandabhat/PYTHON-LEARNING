""" Get user input of sentences until he enters "Enter" key
    Assign all sentences into a list
    find the number of words entered
    find the number of words which has "a" entered in it
"""

def words_entered(sentnce):
    word=0
    aword=0
    vowel = "a"
    for words in sentnce :
        aword = aword + words.count(vowel)        
        word = word + len(words.split())
    print "Total words entered is ", word
    print "Total words which has","'a'","in it is :", aword
        
   

def get_name():
    """ This function fetches the sentence from user until he hits
        "Enter" key without any words prior to it.
        Appends all sentences into a list
    """
    snt =[]
    while True :
        sent=raw_input("Enter a sentence of your choice : ")
        if sent == "" :
            break
        snt.append(sent)
    return snt
   

# Main starts from here
sentence = get_name()
words_entered(sentence)



