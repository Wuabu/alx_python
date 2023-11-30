def pow(a, b):
    # Base case: any number to the power of 0 is 1
    if b == 0:
        return 1
    
    # Initialize result to the base value
    result = a
    
    # Multiply 'result' by 'a' 'b-1' times
    for _ in range(1, b):
        result *= a
    
    return result
