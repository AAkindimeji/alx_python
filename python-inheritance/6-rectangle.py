class BaseGeometry:
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as an integer and checks if it is greater than 0."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Instantiates a Rectangle with given width and height."""
        self.integer_validator("_Rectangle__width", width)
        self.integer_validator("_Rectangle__height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
