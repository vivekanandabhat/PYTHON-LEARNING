""" Reads user input on marks scored in English, Science & Maths.
    English exam marks = 80; Science = 90 & Maths = 100.
    Student scores 1st class if each individual subject score is >=90%
    2nd class if each individual subject score is >=75%
    Average if each individual subject score > 35% and not failed
    Failed if score is <=35%
"""


def result(eng_avg, sci_avg, maths_avg) :

    if (eng_avg<=35 or sci_avg<=35 or maths_avg<=35):
        print "But alas Vivek Failed in the exam!"
    elif (eng_avg>=90 and sci_avg>=90 and maths_avg>=90):
        print "Vivek passed in FIRST CLASS!!!"
    elif (eng_avg>=75 and sci_avg>=75 and maths_avg>=75):
        print "Vivek passed in SECOND CLASS!!"
    else :
        print "Vivek passed with Average Grades!"


def average_scores(english, science, maths) :

    english=(english/80)*100
    science=(science/90)*100
    Average=( english + science + maths ) / 3

    
    print "English % is ", english
    print "Science % is ", science
    print "Maths % is ", maths
    print "The Total Average for Vivek is : ", Average
    return float(english), float (science), float(maths)


def get_marks():
    eng_marks=raw_input("Enter the mark obtained for Vivek in English between 1 and 80 : ")
    sci_marks=raw_input("Enter the mark obtained for Vivek in Science between 1 and 90 : ")
    math_marks=raw_input("Enter the mark obtained for Vivek in Mathematics between 1 and 100 : ")
    return float(eng_marks), float(sci_marks), float(math_marks)

# Main starts from here
eng, sci, math = get_marks()
avg_eng, avg_sci, avg_maths = average_scores(eng, sci, math)
result(avg_eng, avg_sci, avg_maths)
