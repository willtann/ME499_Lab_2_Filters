#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_2_Filters
import math
import random


def reverse_i(r1):
    r2 = []  # make an empty list
    l = len(r1) - 1  #
    for i in range(len(r1)):
        r2.append(r1[l - i])
    return r2


def reverse_r(r1):
    reverse = lambda r1: (reverse(r1[1:]) + r1[:1] if r1 else [])
    return reverse(r1)


if __name__ == "__main__":
    r1 = [1, 2, 3, 4, 5, 6, 7, 8, 'yes']

    print(reverse_i(r1))
    print(reverse_r(r1))
    xyz = 1
    print(lambda xyz)

