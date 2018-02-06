#!/usr/bin/python
def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here
    max_value = None
    for item in t:
        if type(item) is int:
            mv = item
        else:
            mv = max_val(item)

        if mv > max_value or max_value is None:
            max_value = mv
    return max_value


def test(val, shouldbe):
    print '========'
    print 'testing {}'.format(val)
    print 'result is {}, should be {}'.format(max_val(val), shouldbe)


test01 = [0, 1, 2, (2, 4, 6), range(0, 100)]
test(test01, 99)

test02 = [range(-100, -1, 10)]
test(test02, -10)

test03 = [(2, 5, 9), [-1, 10, 1], 100, (-1, -10, -40)]
test(test03, 100)

test04 = [89, -10, 0, 10, 20, (100, 100, 99)]
test(test04, 100)

test05 = [(-10,), 1, -10, -900000, [1]]
test(test05, 1)

test06 = (5, (1, 2), [[1], [2]])
test(test06, 5)

test07 = (5, (1, 2), [[1], [9]])
test(test07, 9)

test08 = (5, (1, 2, [10, [20], 10, 1, (range(3))]), [[1, 9], [9]])
test(test08, 20)
