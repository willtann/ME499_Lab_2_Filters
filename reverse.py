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
    r2 = r1.copy()  # Making a copy of list 'A' so we don't alter it

    def nested_write(r2):  # nested function
        if r2 == :
            r1.pop(0)  # call last element
            r3.append(nested_write(r1[:]))  # writes element and doesn't erase that element

    print(r2)


if __name__ == "__main__":
    r1 = [1, 2, 3, 4, 5, 6, 7, 8, 'yes']

    print(reverse_i(r1))
    print(reverse_r(r1))


