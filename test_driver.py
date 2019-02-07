# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:33:00 2019

@author: xxzac
"""

#from basic_examples import * #import all functions from a file
#from basic_examples import print_all #import only one function
import basic_examples as be
be.print_all('yeet','yah')

#sorting
a= [1,7,5,9,2,6,4,4,2]
b= list(a)
print(a)
a.sort()
print(a)
print("------")
print(b)
print(sorted(b))
print(b)
print("------")
tups = [('a', 4), ('y',1), ('k', 12), ('m', 6)]
print(sorted(tups, key=lambda x: x[1]))
print("------")
print(sorted(tups, key = lambda x: x[0]))