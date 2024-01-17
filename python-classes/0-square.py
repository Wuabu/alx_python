class Square:
    def __init__(self, size):
        self.__size = size

# Example usage:
square_instance = Square(5)
# Accessing the size attribute directly will result in an AttributeError
# print(square_instance.__size)
