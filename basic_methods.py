class Calculator:
    def add(self, n1, n2):
        return n1 + n2

    def subtract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        return n1 / n2 if n2 else 0


n1 = float(input("Insert a number: "))
n2 = float(input("Insert another number: "))
calculator = Calculator()
print(calculator.add(n1, n2))
print(calculator.subtract(n1, n2))
print(calculator.multiply(n1, n2))
print(calculator.divide(n1, n2))
