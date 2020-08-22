#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

"""
The Smith - Waterman Algorithm
    is an NLP and Bioinformatics algorithm 
    which finds the similarity two strings/genes.

This is a local alignment algorithm and
the strings can be found by backtrace

-- Termination steps: --
    
To find the best local alignment
        Fopt = max i, j F(i, j)

To find all local alignments "scoring > t"
        find all F(i, j) and trace back 
"""

def smith_waterman(X, Y, d, s):
    #Initialization
    N, M = len(X), len(Y)
    F = np.zeros((N, M))
    #The first row and column must set as zero
    #Here, F is a zero matrix, no need to set
    
    #Iteration
    for i in range(1, N):
        for j in range(1, M):
            F[i, j] = max(0,
                         F[i - 1, j] - d,
                         F[i, j - 1] - d,
                         F[i - 1, j - 1] + s(X[i], Y[j]))
    #Termination
    return F, F[i, j]

F, dist = smith_waterman("hello", "yellow", d=-1, s=lambda x,y: 0 if x == y else 2)
print(F)
print(dist)