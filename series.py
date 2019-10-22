#----------------------------------------------------------------------#
# Title: Lesson 2 fibonacci, lucas and sum_series exercise for Python 210 Class
# Dev: JPatten
# Date Oct 16, 2019
# ChangeLog: (When, Who, What)
# Purpose:  Demonstrate looking, the modulo operator and using the 
#    IF statement to control logic flow
#
#----------------------------------------------------------------------#

def fibonacci(m,a=None,b=None,c=None,l=None):
 #   print("fibonacci called with", l)
 #   print("first line a=",a,"b=",b,"c=",c,"l=",l,"m=",m)
    if m < 0:
 #       print("Invalid number. Must be > 0 m=",m)
        return m
    if a is None:
        a=0
        b=0
        c=1
        l=0
    elif c==0:
        a=1
        b=0
    c=a+b
#    print("first if a=",a,"b=",b,"c=",c,"l=",l,"m=",m)
    a=b
    b=c
#    if l==0:
#        c=0
#    elif l==1:
#        c=1
    l=l+1
#    print("a=",a,"b=",b,"c=",c,"l=",l,"m=",m)
    if l > m:
        print(c)
        return c  
    else:
        fibonacci(m,a,b,c,l)
    return 


def lucas(m,a=None,b=None,c=None,l=None):
 #   print("fibonacci called with", l)
    if m< 0:
 #       print("Invalid number. Must be > 0 m=",m)
 #       print("line 48")
        return m
    if m==0:
        return 2
    if m==1:
        return 1
    if a is None:
        a=0
        b=2
        c=1
        l=2
 #       print("if a is none  a=",a,"b=",b,"c=",c,"l=",l,"m=",m)
 #       print("line 58")
    a=b
    b=c
    c=a+b
 #   print("a=",a,"b=",b,"c=",c,"l=",l,"m=",m)
    l=l+1
    if l >= m+1:
 #       print("line 76")
        print(c)
        return c  
    else:
        lucas(m,a,b,c,l)
    return 


def sum_series(m,a=None,b=None,c=None,l=None):
 #   print("fibonacci called with", l)
    if a is None:
        return fibonacci(m)
    if a==2 and b==1:
        return lucas(m)
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

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7
    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")


