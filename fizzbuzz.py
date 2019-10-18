#----------------------------------------------------------------------#
# Title: Lesson 2 FizzBuzz exercise for Python 210 Classe
# Dev: JPatten
# Date Oct 16, 2019
# ChangeLog: (When, Who, What)
# Purpose:  Demonstrate looking, the modulo operator and using the 
#    IF statement to control logic flow
#
#----------------------------------------------------------------------#



def fizzbuzz():
    for i in range(100):
        if (i+1)%3==0 and (i+1)%5==0:
            print ('FizzBuzz')
        elif  (i+1)%3==0:
            print('Fizz')
        elif  (i+1)%5==0:
            print('Buzz')
        else:
            print(i+1)
 