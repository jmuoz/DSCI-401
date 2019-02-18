# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:20:04 2019

@author: xxzac
"""

def print_all(w,x,y=1,z=2):
    print(w)
    print(x)
    print(y)
    print(z)
#%%
def print_options(x,y,*z):
    print(x)
    print(y)
    print(z)
#%% Return all unique combinations
def gen_combs(elems, k):
    if k == len(elems):
        return [elems]
    if k == 1:
        return [[x] for x in elems]
    else:
        return [[elems[0]] + c for c in gen_combs(elems[1:], k-1)] + gen_combs(elems[1:], k)
#%%