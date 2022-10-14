# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:07:15 2017

@author: chand
"""
#Tower of Hanoi
def printmove(fr, to):
    print("Move from " +str(fr)+" to ", str(to))
def Tower(n, fr, to, spare):
    if n==1:
        printmove(fr, to)
    else:
        Tower(n-1, fr, spare, to)
        Tower(1, fr, to, spare)
        Tower(n-1, spare, to, fr)
        