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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    def __init__(self, size):
        """Instantiates a Square with given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the Square."""
        return "[Rectangle] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
