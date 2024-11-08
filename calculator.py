"""Module providing a calculator class responsible for arithmetic operations on user input."""
class Calculator:
    def __init__(self, arg1: float, arg2: float):
        #Importing user input:
        self._arg1 = arg1
        self._arg2 = arg2

    def sum(self):
        return self._arg1 + self._arg2

    def subtract(self):
        return self._arg1 - self._arg2

    def multiply(self):
        return self._arg1 * self._arg2

    def divide(self):
        return self._arg1 / self._arg2
