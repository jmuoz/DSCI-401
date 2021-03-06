# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:02:00 2019

@author: Zachary Johnson
"""
#%%
def flat(e):
    if type(e[0]) == list:
        return flat(e[0]) + flat(e[1:])
    return e[0] + flat(e[1:])
            
#I don't know why this doesnt work, I can't even really test it because it just runs forever  
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
#spiral: data structure? list of lists? 
#dirs = [(0,-1), (1,0), (0,1), (-1,0)]
#x,y = (starting coord)
#curr_num = n = -1
#while curr_num >= 0:
#   matrix[x][y]=curr_num
#   if change_direction:
#       current_direction = (next direction)
#   x,y += curr_direction
#   curr_num -= 1
#THE ABOVE IMPLEMENTATION DOESN'T WORK BECAUSE PYTHON DOES NOT ALLOW YOU TO UPDATE MULTIPLE
#VARIABLES WITH THE += or -= OPERATORS
#you may be able to get it to work if you create all the coordinates beforehand

def spiral(dim, cor):
    matrix = [[0 for i in range(dim)] for j in range(dim)]
    nums = list(range(dim * dim))
    dirs = [(1,0),(0,-1),(-1,0),(0,1)]
    if dim == 1:
        matrix[0].append(0)
        return matrix
    else:
        curr_num = nums[-1]
        if cor == 1:
            x,y = (0,0)
            curr_dir = dirs(0)
            while curr_num >= 0:
                matrix[x][y] = curr_num
                
        
#%% trying an iterative approach, doesn't work...
def flatten(e):
    out = [] #this is why it doesnt work right here; whenever it recurses it deletes this list's contents... or something
    for i in e:
        if type(i) == list:
            flatten(i)
        else:
            out.append(i)
    return out
#%%this sort of works but not really
def flat2(e):
    out = []
    for list in e:
        for i in list:
            out.append(i)
    return out
#%% maybe if I try it again I'll have a better shot 
def spiral2(dim, corner):
    matrix = [[0 for i in range(dim)] for j in range(dim)]
    dirs = {'right':(1,0), 'down':(0,-1),'left':(-1,0),'up':(0,1)}
    clock = {'right':'down', 'down':'left','left':'up','up':'right'}
    curr_num = dim*dim-1
    while curr_num >= 0:
        if corner == 1:
            curr_dir = 'right'
            x,y = (0,0)
            q,r = dirs[curr_dir]
            matrix[x][y] == curr_num
            if ???: #I don't know how to tell it when to change direction...
                curr_dir = clock[curr_dir] #change direction
                q,r = dirs[curr_dir]
                x,y = x + q, y + r
                curr_num -=1
            else:
                x,y = x + q, y + r
                curr_num-=1
        if corner == 2:
            curr_dir = 'down'
            x,y = (-1,0)
            q,r = dirs[curr_dir]
            matrix[x][y] == curr_num
            if ???: #I don't know how to tell it when to change direction...
                curr_dir = clock[curr_dir] #change direction
                q,r = dirs[curr_dir]
                x,y = x + q, y + r
                curr_num -=1
            else:
                x,y = x + q, y + r
                curr_num-=1
        if corner == 3:
            curr_dir = 'up'
            x,y = (0,-1)
            q,r = dirs[curr_dir]
            matrix[x][y] == curr_num
            if ???: #I don't know how to tell it when to change direction...
                curr_dir = clock[curr_dir] #change direction
                q,r = dirs[curr_dir]
                x,y = x + q, y + r
                curr_num -=1
            else:
                x,y = x + q, y + r
                curr_num-=1
        if corner == 4:
            curr_dir = 'left'
            x,y = (-1,-1)
            q,r = dirs[curr_dir]
            matrix[x][y] == curr_num
            if ???: #I don't know how to tell it when to change direction...
                curr_dir = clock[curr_dir] #change direction
                q,r = dirs[curr_dir]
                x,y = x + q, y + r
                curr_num -=1
            else:
                x,y = x + q, y + r
                curr_num-=1
    return matrix
#%%
