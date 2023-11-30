def fibonacci_sequence(n):
    # Check if n is not a positive integer
    if not isinstance(n, int) or n <= 0:
        return []

    # Initialize the Fibonacci sequence with the first two numbers
    sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth number
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# Test cases
