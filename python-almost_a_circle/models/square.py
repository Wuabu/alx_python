#!/usr/bin/python3
"""Module containing the Square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance with size, x, y, and id."""
        # Call the constructor of the Rectangle class with id, x, y, size, and size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
