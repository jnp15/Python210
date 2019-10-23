#----------------------------------------------------------------------#
# Title: Lesson 2 fibonacci, lucas and sum_series exercise for Python 210 Class
# Dev: JPatten
# Date Oct 16, 2019
# ChangeLog: (When, Who, What)
# Purpose:  Demonstrate looking, the modulo operator and using the 
#    IF statement to control logic flow
#
#----------------------------------------------------------------------#

def fibonacci(m):
    ''' This routine takes four parameter and can calculte the fibonacci,
     lucus or generic series'''
 
 #   print("fibonacci called with", l)
 #   print("first line a=",a,"b=",b,"c=",c,"l=",l,"m=",m)
    if m < 0:
        print("Invalid number. Must be > 0 m=",m)
        return m
    if m==0:
        return 0
    if m<3:
        return 1
    return fibonacci(m-1)+fibonacci(m-2)


def lucas(m):
 #   print("fibonacci called with", l)
    if m < 0:
        print("Invalid number. Must be > 0 m=",m)
    if m == 0:
        return 2
    if m == 1:
        return 1
    return lucas(m-1)+lucas(m-2)

def sum_series(m,a=0,b=1):
#   print('m=',m,' a=',a,' b=',b)
   if m==0:
        return a
   if m==1:
        return b
   return sum_series(m - 2, a, b) + sum_series(m - 1, a, b)

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
 #   assert fibonacci(1) == 1
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


