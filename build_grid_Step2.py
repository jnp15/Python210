
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

def makeboxPart2(n):
#print first line
  print('+ ', end='')
  for i in range(2):
     print ('- '*int(n/2),'+ ', end='')
  print('')
 #print first box
  for i in range(2):
     for i in range(int(n/2)):
       print ('|',' '*int(n), end='')
       for i in range(int(1)):
          print ('|',' '*(int(n)), end='')
       print('|')
     print('+ ', end='')
     for i in range(int(2)):
       print ('- '*(int(n/2)),'+ ', end='')
     print('')