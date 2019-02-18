# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:29:22 2019

@author: xxzac
"""

def prod(*s):
    if len(s)==1:
        return [(i) for i in s[0]]
    else:
        rest = prod(*s[1:])
        return [x + q for x in s[0] for q in rest]