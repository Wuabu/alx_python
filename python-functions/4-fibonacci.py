def fibonacci_sequence(n):
    
    if not isinstance(n, int) or n <= 0:
        return []

    
    sequence = [0, ]

    
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


