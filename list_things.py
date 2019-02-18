# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 18:58:44 2019

@author: xxzac
"""

def reverse(entry):
    out = []
    e = 1
    for i in entry:
        r = -e
        out.append(entry[r])
        e+=1
    print(out)

reverse([1,2,3])
reverse([0,1,2,3,4,5,6,7,8,9])
#%% I looked up what recursion was, it means repeated? But I also think its some kind of techique...
# don't really know what to do...
def repeat_reverse(entry, x):
    if type(x) == int:
        out = []
        e = 1
        for i in entry:
            r = -e
            out.append(entry[r])
            e+=1
        while x!=0:
            print(out)
            x-=1
    else:
        print('The second argument must be a whole number.')

repeat_reverse([1234,3,54,777,666], 2)
#%%
def nth_element(entry, x):
    out = []
    if x==1:
        print(entry)
    elif type(x) == int:
        marker = -1 #zero-indexing is annoying
        iteration = int(len(entry)/x)
        while iteration>0:
            marker+=x
            out.append(entry[marker])
            iteration-=1
        print(out)
    else:
        print("X must be a whole number.")
#%%
test_list = [12,3,54,77,66,666,9,8]
test_list2 = [2,3,4,5,6,7,8,9]
nth_element(test_list,2)
nth_element(test_list,3)
#%%
def dot_product(entry1, entry2):
    if len(entry1) == len(entry2):
        out = []
        marker = 0
        for i in entry1:
            out.append(entry1[marker]*entry2[marker])
            marker+=1
        print(sum(out))
    else:
        print('Both lists must be the same dimensions.')
#%%
dot_product(test_list, test_list2)
#%% recursion
def sumrange(x,y):
    if x == y:
        return x
    return sumrange(x,y-1)+y
sumrange(1,5)
#%%
def reversion(entry):
    if entry == []:
        return []
    return[entry[-1]]+ reversion(entry[:-1])
#%%
reversion(test_list)
#%% Algorithm design -  recursion again, fibonacci numbers, arbitrary first and second elements
def f_sequence(a,b,n):
    if n == 1:
        return a
    if n == 2:
        return b
    else:
        return f_sequence(a, b, n-1) + f_sequence(a, b, n-2)
#%%

