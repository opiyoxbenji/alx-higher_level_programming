#!/usr/bin/python3

class Square:
    """
    This is the Square class.
    It represents a square and provides a method to calculate its area.
    """
    
    def square_area(self, side_len):
        """
        Calculate the area of the square.

        :param side_len: Length of one side of the square.
        :return: The area of the square.
        """
        self.side_len = side_len
        area = self.side_len ** 2
        return area
