def viett(a,b,c):
    """Search of roots of quadratic equation"""
    pass
    D = pow (b,2) - 4*a*c
    q = c / a
    p = -b / a
    if D < 0:
        raise ValueError("X1 and X2 are complex")
    try:
        x1 = 1
        while x1 <= max (abs(p),abs(q)):
            if x1*(-p - x1) == q: 
                return x1, -p + x1
            if -x1*(-p + x1) == q:
                return x1, p - x1                                
            x1 += 1 
    except UnboundLocalError as err:
        print ("Roots aren't integer")


print viett(1,-20,84)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
