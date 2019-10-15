#----------------------------------------------------------------------#
# Title: Lesson 2 exercise for Python 210 Classes
# Dev: JPatten
# Date October 13, 2019
# ChangeLog: (When, Who, What)
# Purpose:  This program demonstrates how create a grid with user defined
#    rows, columns, column widths and row heiths
#
#----------------------------------------------------------------------#
# -*- coding: utf-8 -*-

def makebox(r,c,w,h):
#print first line
  print('+', end='')
  for i in range(c):
     print ('-'*w,'+', end='')
  print('')
 #print first box
  for i in range(r):
     for i in range(h):
       print ('|',' '*w, end='')
       for i in range(c-1):
          print ('|',' '*w, end='')
       print('|')
     print('+', end='')
     for i in range(c):
       print ('-'*w,'+', end='')
     print('')