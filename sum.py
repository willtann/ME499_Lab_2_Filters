#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_2_Filters
import math


def sum_i(l1):
    counter = 0
    #  for each element in the list add it to the total
    y = int(len(l1))
    for x in range(y):
        counter.append(l1(x))
    return counter


l1 = [1, 4, 5]
print(sum_i(l1))

print(sum(l1))