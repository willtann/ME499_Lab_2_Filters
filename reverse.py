#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_2_Filters
import math
import random


def reverse_i(r1):
    # make an empty list the same length as input list
    i = 0
    l = len(r1)
    length = l - 1
    r2 = r1.copy()
    print('r1(length)...', r1[length])
    print('length...', length)
    print('r2(i)...', r2[i])
    print('i...', i)
    for i in range(len(r1)):
        r2[i] = r1[-length]
        i += 1
        length()
        return r2


def reverse_r(r1):
    r2 = []
    if len(r1) > 1:
        r2[len(r1-1)]
        print(r2)

if __name__ == "__main__":
    r1 = [1, 2, 3, 4, 5]
    print(reverse_i(r1))
