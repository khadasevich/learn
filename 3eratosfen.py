def eratosfen (n):
    """Eratosphen method"""
    pass
# creation of range
    a = [i for i in range(0,n)]
    a[1] = 0
    m = 2
# Eratosfen can do it
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
# New range with prime numbers
    b = set(a)
    b.remove(0)
    return b 

print "Enter n ", eratosfen(int(input()))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
       
    
