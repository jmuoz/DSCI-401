# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:10:50 2019

@author: xxzac
"""
def flatten(*entry):
    out = []
    if type(entry[i]) != list:
           out.append(entry[i])
    if type(entry[i]) == list:
        out.append(flatten(entry[i])
    return out                                                                                         