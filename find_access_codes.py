#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:15:59 2021

@author: johnsenaakoto
"""

def solution(l):
    l1 = []
    l2 = []
    
    for i in range(1, len(l)):
        l1.append(sum([1 if (l[i] % l[q] == 0) else 0 for q in range(i)]))
        l2.append(sum([1 if (l[q] % l[i] == 0) else 0 for q in range(i+1, len(l))]))
        
    return(sum([num1 * num2 for num1,num2 in zip(l1, l2)]))
        
print(solution([1, 2, 3, 4, 5, 6]))