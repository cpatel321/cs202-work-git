"""This module provides a simple calculator implementation with basic arithmetic operations."""

class Calculator:
    """A calculator class that performs basic arithmetic operations and maintains calculation history."""

    def __init__(self, x, y):
        """Initialize calculator with two numbers.
        
        Args:
            x (float): First number for calculations
            y (float): Second number for calculations
        """
        self.num1 = x
        self.num2 = y
        self.history = []

    def add(self):
        """Add two numbers and print the result.
        
        Returns:
            float: Sum of the two numbers
        """
        result = self.num1 + self.num2
        print(f"{self.num1} + {self.num2} = {result}")
        # return result

    def subtract(self):
        """Subtract second number from first number and print the result.
        
        Returns:
            float: Difference between the two numbers
        """
        r = self.num1 - self.num2
        print(f"{self.num1} - {self.num2} = {r}")
        # return r

    def multiply(self):
        """Multiply two numbers and print the result.
        
        Returns:
            float: Product of the two numbers
        """
        result = self.num1 * self.num2
        print(f"{self.num1} * {self.num2} = {result}")
        # return self.num1*self.num2

    def divide(self):
        """Divide first number by second number and print the result.
        
        Returns:
            float: Quotient of the division, or None if dividing by zero
        """
        if self.num2 != 0:
            result = self.num1 / self.num2
            print(f"{self.num1} / {self.num2} = {result}")
            # return self.num1/self.num2
        else:
            print("Cannot divide by zero")
            # return None