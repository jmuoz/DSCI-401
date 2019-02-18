# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:33:00 2019

@author: xxzac
"""

#from basic_examples import * #import all functions from a file
#from basic_examples import print_all #import only one function
import basic_examples as be
#be.print_all('yeet','yah')

#sorting
a= [1,7,5,9,2,6,4,4,2]
b= list(a)
#print(a)
a.sort()
#print(a)
#print("------")
#print(b)
#print(sorted(b))
#print(b)
#print("------")
tups = [('a', 4), ('y',1), ('k', 12), ('m', 6)]
#print(sorted(tups, key=lambda x: x[1]))
#print("------")
#print(sorted(tups, key = lambda x: x[0]))
#%% square
#p = [x*x for x in range(1,6)]
#print(p)
#%%
#even_squares = [x for x in [y*y for y in range(1,101)]] if x % 2 != 0
#%%
#zip, can transform a matrix's rows to columns
ziperino = list(zip([1,2,3],[4,5,6],[7,8,9]))
print(ziperino)
#%%
def f_sequence(a,b,n, cache={}):
    if n in cache:
        return cache[n]
    if n == 1:
        return a
    if n == 2:
        return b
    else:
        cache[n] = f_sequence(a, b, n-1, cache) + f_sequence(a, b, n-2, cache)
        return cache[n]
#%%
def prod(*s):
    if len(s)==1:
        return [(i) for i in s[0]]
    else:
        rest = [prod(*s[1:])
        [[x] + q for x in s[0] for q in rest]
        
       