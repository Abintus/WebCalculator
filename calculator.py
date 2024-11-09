"""
Module providing a calculator class responsible for arithmetic operations on user input.

Classes:
    Calculator

"""
class Calculator:
    """
    Calculator class responsible for arithmetic operations on user input.

    Attributes:
        _arg1: float
            First number for arithmetic operations.
        _arg2: float
            Second number for arithmetic operations.

    Methods:
        sum(self)
            Performs addition of class attributes.
        subtract(self)
            Performs subtraction of class attributes.
        multiply(self)
            Performs multiplication of class attributes.
        divide(self)
            Performs division of class attributes.

    """
    def __init__(self, arg1: float, arg2: float):
        #Importing user input:
        self._arg1 = arg1
        self._arg2 = arg2

    def sum(self):
        """
        Function performs addition of object's attributes.
        Returns:
        String
        """
        return self._arg1 + self._arg2

    def subtract(self):
        """
        Function performs subtraction of object's attributes.
        Returns:
        String
        """
        return self._arg1 - self._arg2

    def multiply(self):
        """
        Function performs multiplication of object's attributes.
        Returns:
        String
        """
        return self._arg1 * self._arg2

    def divide(self):
        """
        Function performs division of object's attributes.
        Returns:
        String
        """
        return self._arg1 / self._arg2
