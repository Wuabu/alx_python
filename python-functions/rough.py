def pow(a, b):
    # Check if b is negative
    if b < 0:
        return "Error: This implementation does not handle negative exponents."
    
    # Initialize result to 1 (a^0 is always 1)
    result = 1
    
    # Multiply 'result' by 'a' 'b' times
    for _ in range(b):
        result *= a
    
    return result

# Test cases
print(pow(2, 2))    # Should print 4
print(pow(98, 2))   # Should print 9604
print(pow(98, 0))   # Should print 1
print(pow(100, -2)) # Should print "Error: This implementation does not handle negative exponents."
print(pow(-4, 5))   # Should print -1024
