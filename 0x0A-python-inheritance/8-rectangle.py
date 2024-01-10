#!/usr/bin/python3
"""
Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry
        Attributes:
            width(int): width of rectangle
            height(height): height of rectangle
    """

    def __init__(self, width, height):
        """Initializes instance of a Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
