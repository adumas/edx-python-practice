#!/usr/bin/python
def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """

    k = len(L) - 1

    def fsum(f1, f2): return lambda x: f1(x) + f2(x)
    print k, L
    if k is 0:
        # print '{} * (x**{})'.format(L[0], k)
        return lambda x: L[0]
    else:
        n = L.pop(0)
        # print '{} * (x**{})'.format(n, k)
        return fsum(lambda x: n * (x**k), general_poly(L))


def test(val):
    print '========'
    print 'testing {}'.format(val)
    print 'result is {}'.format(general_poly(val[0])(val[1]))


testing = (([1, 2, 3, 4], 10),
           ([1, 2, 3], 10),
           ([5], 10),
           ([10, 5, 2, 1], 10))

for item in testing:
    test(item)
