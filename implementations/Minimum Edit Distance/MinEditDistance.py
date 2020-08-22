#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

"""
Minimum Edit Distance
 is an algorithm which finds the differnce between two words.

The difference is calculated by counting the operations:
    -Insertion
    -Deletion
    -Substitution
    
Deafult code runs the Levenshtein Minimum Distance Algorithm.
A pointer is used to add backtrace.
Weights can be changed by the user.
"""

def min_edit_distance(X, Y):
    #Initialization
    N, M = len(X), len(Y)
    D = np.zeros((N, M))
    ptr = np.empty((N, M), dtype=np.str0)
    for i in range(N):
        D[i, 0] = i
    for j in range(M):
        D[0, j] = j
    
    calculate = lambda x, y: 0 if x == y else 2
    
    #Recurrence Relation
    for i in range(1, N):
        for j in range(1, M):
            min_val = D[i - 1, j] + 1
            min_ptr = "←"
            if D[i, j - 1] + 1 < min_val:
                min_val = D[i, j - 1] + 1
                min_ptr = "↑"
            elif D[i - 1, j - 1] + calculate(X[i], Y[i]) < min_val:
                min_val = D[i - 1, j - 1] + calculate(X[i], Y[j])
                min_ptr = '↖'
                    
            D[i, j] = min_val
            ptr[i, j] = min_ptr
    
    #Termination
    return D[N - 1, M - 1], D, ptr
    
diff, D_matrix, pointer = min_edit_distance("intention", "execution")
print(diff)
print(D_matrix)
print(pointer)
