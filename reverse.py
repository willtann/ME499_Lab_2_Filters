#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_2_Filters


def reverse_i(r):
    r1 = []  # make an empty list
    l = len(r) - 1  # since index @0
    for i in range(len(r)):
        r1.append(r[l - i])
    return r1


def reverse_r(r):
    if r:
        return [r.pop()] + reverse_r(r)
    else:
        return []


# if __name__ == "__main__":
#     r = [1, 2, 3, 4, 5, 6, 7, 8, 'yes']
#
#     print(reverse_i(r))
#     print(reverse_r(r))
