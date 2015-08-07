def fib(_list):
    """"Fibonacci is dead"""
    pass
    fib1 = fib2 = fibnew = 1
    _newlist = []
    for element in _list:
        while fibnew < element:
            fibnew = fib1 + fib2
            if fibnew > element:
                _newlist.append(fib2)
            fib1 = fib2
            fib2 = fibnew
        fibnew = fib1 = fib2 = 1    
    return _newlist

print fib([250, 180, 600, 50])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
