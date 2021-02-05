def primesInRange(lowBound, highBound): 
    prime_list = []
    
# Input validation
    if lowBound < 2:
        return None
    if highBound > 1000:
        return None
    if not(isinstance(lowBound, int)):
        return None
    if not(isinstance(highBound, int)):
        return None
    if lowBound > highBound:
        return None
    
    for n in range(lowBound, highBound+1):
        if n == 2:
            prime_list.append(n)
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
        if ((n % 11 == 0) & (n != 11)):
            continue
        if ((n % 13 == 0) & (n != 13)):
            continue
        if ((n % 15 == 0) & (n != 15)):
            continue
        if ((n % 17 == 0) & (n != 17)):
            continue
        if ((n % 19 == 0) & (n != 19)):
            continue
        if ((n % 21 == 0) & (n != 21)):
            continue
        if ((n % 23 == 0) & (n != 23)):
            continue
        else:
            prime_list.append(n)
            
    return prime_list