#!/bin/python3

import sys

def lonely_integer(a):
    if len(a) == 1:
        return a[0]
    i=0
    a.sort()
    # print(a)
    while i+1 < len(a):
        if a[i] != a[i+1]:
            return a[i]
        else:
            i = i + 2
    return a[-1]
        
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
