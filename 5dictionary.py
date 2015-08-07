def dic(d):
    """Program for change keys and values in dictionary"""
    pass
    dnov  = {}
    for key, value in d.items():
        dnov.setdefault(value, []).append(key)
    return dnov

print dic({'a' : 1, 'b' : 2, 'c' : 1, 'j' : 5})

if __name__ == "__main__":
    import doctest
    doctest.testmod()
