
class Calculator:
    def divide(self, dividend: float, divisor: float) -> float:
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend / divisor

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y
