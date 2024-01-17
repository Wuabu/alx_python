class Square:
    def __init__(self, size=0):
        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

# Example usage:
try:
    square_instance = Square(5)
    print(f"Square area: {square_instance.area()}")
except (TypeError, ValueError) as error:
    print(f"Error: {error}")

try:
    invalid_square = Square("invalid")
    print(f"Square area: {invalid_square.area()}")
except (TypeError, ValueError) as error:
    print(f"Error: {error}")
