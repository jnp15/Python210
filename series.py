#----------------------------------------------------------------------#
# Title: Lesson 2 FizzBuzz exercise for Python 210 Classe
# Dev: JPatten
# Date Oct 16, 2019
# ChangeLog: (When, Who, What)
# Purpose:  Demonstrate looking, the modulo operator and using the 
#    IF statement to control logic flow
#
#----------------------------------------------------------------------#



def fibonacci(m,a=None,b=None,c=None,l=None):
 #   print("fibonacci called with", l)
    if a is None:
        a=0
        b=1
        c=1
        l=1
    # do something
    a=b
    b=c
    c=a+b
    l=l+1
#    print("a=",a,"b=",b,"c=",c,"l=",l,"m=",m)
    if l == m:
        print(c)
        return c  
    else:
        fibonacci(m,a,b,c,l)
    return 


def lucus(m,a=None,b=None,c=None,l=None):
 #   print("fibonacci called with", l)
    if a is None:
        a=1
        b=0
    if c is None:
        c=1
        l=1
    # do something
    a=b
    b=c
    c=a+b
    l=l+1
#    print("a=",a,"b=",b,"c=",c,"l=",l,"m=",m)
    if l == m:
        print(c)
        return c  
    else:
        lucus(m,a,b,c,l)
    return 

def sum_series(m,a=None,b=None,c=None,l=None):
 #   print("fibonacci called with", l)
    if a is None:
        a=0
        b=1
    if c is None:
        c=1
        l=1
    # do something
    a=b
    b=c
    c=a+b
    l=l+1
#    print("a=",a,"b=",b,"c=",c,"l=",l,"m=",m)
    if l == m:
        print(c)
        return c  
    else:
        sum_series(m,a,b,c,l)
    return 
