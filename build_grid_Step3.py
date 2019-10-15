
#----------------------------------------------------------------------#
# Title: Lesson 2 Part 3
#Exercise for Python 210 Classes
# Title: Lesson 2 Part 3
# Dev: JPatten
# Date October 13, 2019
# ChangeLog: (When, Who, What)
# Purpose:  This program demonstrates how create a grid with user defined
#    rows, columns, column widths and row heiths
#
#----------------------------------------------------------------------#
# -*- coding: utf-8 -*-

def makeboxPart3(b,w):
#print first line
  print('+', end='')
  for i in range(b): #columns
     print (' -'*w,'+', end='')
  print('')
 #print first box
  for i in range(b): # rows
     for i in range(w):
        for i in range(b):
          print ('|','  '*w, end='')
        print('|')
     print('+', end='')
     for i in range(b):
       print (' -'*w,'+', end='')
     print('')