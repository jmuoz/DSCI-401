# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:02:00 2019

@author: xxzac
"""
#%%
def flat(e):
    if e == []:
        return e
    if type(e[0]) == list:
        return flat(e[0]) + flat(e[1:])
    else:
        return e[0] + flat(e[1:])
#I don't know why this doesnt work     
#%%
x = [[1],[2], [[3,4], 5], 6]
#%%
if type(x[0]) == list:
    print('something')
#%%
def permutations(e):
    if e == []:
        return e
    if len(e) == 1:
        return e
    if len(e) == 2:
        return [e, list(reversed(e))]
    else:
        end = permutations(e[1:])
        
        return [end[z][i:] + [e[0]] + end[z][:i] for i in range(len(e)) for z in range(len(end))]
#%%
permutations([1,2,3,4])
#%%
def powerset(e):
    if e == []:
        return e
    if len(e) == 1:
        return [e, []]
    else:
        end = powerset(e[1:])
        beginning = [[e[0]] + i for i in end]
        return beginning + end
#%%
powerset([1,2,3,4])
#%%
#Spiral made my head hurt.
    