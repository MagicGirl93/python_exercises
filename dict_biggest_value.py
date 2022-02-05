def f(x):
    """Return the first ascending KEY ordering of a dictionary
    based on the second biggest value that is given in a dictionary
    biggest value that is given in a dictionary"""

    list_val = list(x.values())
    list_values1 = set(list_val)
    try:
        list_values1.remove(None)
    except:
        pass

    list_values2 = list(list_values1)
    list_values2.sort(reverse=True)
    if len(list_values2) <= 1:
        return None
    else:
        v = list_values2[1]

    l2 = []
    for k in x.keys():
        if x.get(k) == v:
            l2.append(k)

    l2.sort()

    return l2[0]


assert (f({'a': 1, 'b': 2, 'c': 2, 'd': 500})) == 'b'
assert (f({'a': 0, 'b': 0, 'c': 2, 'd': 500})) == 'c'
assert (f({'a': None, 'b': None, 'c': None, 'd': 500})) is None
