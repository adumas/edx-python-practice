#!/usr/bin/python


def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    import math

    closest = math.log10(num) / math.log10(base)
    boundsfun = [math.floor, math.ceil]

    lu = [f(closest) for f in boundsfun]
    diff = [abs(num - base**exp) for exp in lu]

    if diff[1] >= diff[0]:
        ix = 0
    else:
        ix = 1

    return int(boundsfun[ix](closest))


"""
closest_power(3,12) returns 2
closest_power(4,12) returns 2
closest_power(4,1) returns 0
"""

print closest_power(3, 12)
print closest_power(4, 12)
print closest_power(4, 1)
print closest_power(2, 192.0)
