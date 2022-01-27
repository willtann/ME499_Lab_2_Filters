#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_2_Filters
import math
import random


def sum_i(l1):
    counter = 0
    x = 0
    #  for each element in the list add it to the total
    y = int(len(l1))
    for x in range(y):  # count up and add each iteration to total
        counter += l1[x]
        x += 1
    return counter


def sum_r(l1):
    # If list is longer than one number there is a sum to  be found
    if len(l1) > 1:
        return l1[0] + sum_r(l1[1:])
    else:
        return l1[0]  # no sum... just the integer itself


if __name__ == "__main__":
    l1 = []
    # 100 examples testing against our custom factorial function
    for i in range(100):
        l = random.randint(0, 15)  # get random int each time
        l1.append(l)  # making a list
        assert sum_i(l1) == sum_r(l1)  # test each number in each function
