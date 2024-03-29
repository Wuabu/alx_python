"""
This module defines a Square class.

The Square class represents a square geometric shape and has a private
instance attribute for the size.

Example:
    square = Square(5)
    print(square.get_area())  # Output: 25
"""

class Square:
    """This class defines a Square.

    Attributes:
        __size (int): Private instance attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        
        type(size) == int
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size


    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Method to retrieve the size of the Square instance."""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size attribute.

        Args:
            value (int): The value to set as the size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Prints the square using the character #.

        If size is equal to 0, prints an empty line.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)