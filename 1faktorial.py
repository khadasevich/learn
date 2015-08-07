def fakt1(a):
    "Factorial"
    pass
    i = 0 
    fak = 1
    if  a < 0:
        raise ValueError("a must be >=0")
    while i < a:
        i += 1
        fak *= i
    return fak
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

def fakt2(b):
    if b < 0:
        raise ValueError("b must be >=0")
    if b == 0:
       return 1
    return fakt2(b-1) * b

print "Enter integer positive number", fakt1(int(input()))
print "Enter integer positive number", fakt2(int(input()))

if __name__ == "__main__":
    import doctest
    doctest.testmod() 
