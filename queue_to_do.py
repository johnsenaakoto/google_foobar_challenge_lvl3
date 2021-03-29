#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:49:28 2021

@author: johnsenaakoto
"""

def solution(start, length):
    checksum = 0
    current = start
    current_len = length
    while current_len > 0:
        checksum ^= computeXOR(current) ^ computeXOR(current + current_len)
        current += length
        current_len -= 1

    return checksum

def computeXOR(n):
    """
    Return 0^1^2^....^(n-1)
    """
    if n == 0:
        return 0
    
    # if n-1 is multiple of 4 
    if (n-1) % 4 == 0:
        return n-1
    # If n-1 % 4 gives remainder 1
    elif (n-1) % 4 == 1:
        return 1
    # If n%4 gives remainder 2
    elif (n-1) % 4 == 2:
        return n
    else:
        return 0
    
print(solution(17,4))