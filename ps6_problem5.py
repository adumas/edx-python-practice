#!/usr/bin/python
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size - i - 1] == e:
            return True
        if L[i] < e:
            return False
    return False


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)


def test(L, e):
    print("for list {} and search term {}".format(L, e))
    print('search yields: {}'.format(search(L, e)))
    print('newsearch yields: {}'.format(newsearch(L, e)))


test([0, 6, 9], 3)
test([0, 6, 9, 12, 19, 21], 13)
test([0, 6, 9, 12, 19, 21], 12)
test(range(0, 20), 13)
test([0, 1], 0)
test([], 13)

modSwapSort([9, 8, 7, 12])
modSwapSort([1, 0])
modSwapSort(range(30))
