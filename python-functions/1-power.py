def pow(a, b):
   
    if b == 0:
        return 1
    
    if b < 0:
        return 1 / pow(a, -b) 
   
    result = a
    
    
    for _ in range(1, b):
        result *= a
    
    return result

#print (pow (10, -2))
