def primesInRange(lowBound, highBound):   
    primeList = []
    for n in range(lowBound, highBound):
        if n == 1: 
            continue
        if n == 2:
            primeList.append(n)
        if n % 2 == 0:
            continue
        if ((n % 3 == 0) & (n != 3)):
            continue
        if ((n % 5 == 0) & (n != 5)):
            continue
        if ((n % 7 == 0) & (n != 7)): 
            continue
        if ((n % 9 == 0) & (n != 9)):
            continue
        else:
            primeList.append(n)
            
    return primeList