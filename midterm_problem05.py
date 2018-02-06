#!/usr/bin/python


def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    valueKeys = []
    for key in aDict:
        if aDict[key] == target:
            valueKeys.append(key)

    return sorted(valueKeys)


adict = {'buffalo': 'tea', 'ham': 'tea', 'mint': 'flavor', 'carpark': 'tea'}
print keysWithValue(adict, 'tea')
