#!/usr/bin/python


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    return sum(map(lambda x, y: x * y, listA, listB))


print dotProduct([1, 2, 3], [4, 5, 6])
print dotProduct([2, 2, 3], [8, 8, 8])
