#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

"""
The Needleman - Wunsch Algorithm
    is an NLP and Bioinformatics algorithm which 
    finds the similarity between two strings/genes.
    
This algorithm fins a global alignment.

    d: deletion/insertion
    s: substitution
"""

def needleman_wunsch(X, Y, d, s):
    #Initialization
    N, M = len(X), len(Y)
    D = np.zeros((N, M))
    for i in range(1, N):
        D[i, 0] = -i * d
    for j in range(1, M):
        D[0, j] = -j * d
    
    #Recurrence Relation
    for i in range(1, N):
        for j in range(1, M):
            D[i, j] = max(D[i - 1, j] - d,
                         D[i, j - 1] - d,
                         D[i - 1, j - 1] + s(X[i], Y[j]))
            
    #Termination
    return D, D[N - 1, M - 1]

D, dist = needleman_wunsch('hello', 'yellow', d=-1, s=lambda x, y: 0 if x == y else 2)
print(D)
print(dist)
