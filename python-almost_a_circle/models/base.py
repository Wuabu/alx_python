"""Module containing the Base class."""
class Base:
    """Base class for managing id attribute."""

    # Private class attribute
    __nb_objects = 0

    # Class constructor
    def __init__(self, id=None):
        """Initialize instance with id."""
        # If id is not None, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        # If id is None, increment __nb_objects and assign the new value to id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects