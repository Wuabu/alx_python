#!/usr/bin/python3
"""Module containing the Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Rectangle class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance with width, height, x, y, and id."""
        # Call the constructor of the Base class with id
        super().__init__(id)

        # Set private instance attributes with public getters and setters
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area value of the Rectangle."""
        return self.width * self.height
# # Usage example
# if __name__ == "__main__":
#     # Creating instances of the Rectangle class
#     rect1 = Rectangle(10, 5)
#     print(rect1.id)  # Output: 1
#     print(rect1.width)  # Output: 10
#     print(rect1.height)  # Output: 5
#     print(rect1.x)  # Output: 0
#     print(rect1.y)  # Output: 0

#     rect2 = Rectangle(2, 3, 4, 1, 7)
#     print(rect2.id)  # Output: 7
#     print(rect2.width)  # Output: 2
#     print(rect2.height)  # Output: 3
#     print(rect2.x)  # Output: 4
#     print(rect2.y)  # Output: 1
