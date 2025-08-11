# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Print calculation type and return the product of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
