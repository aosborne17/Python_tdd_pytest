class Calc:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def cm_to_inches(self, num1):
        return num1 / 2.5

    def modulo(self, num1, num2):
        if num1 % num2 == 0:
            return True
        elif num1 % num2 != 0:
            return False




simple_calc = Calc()

print(simple_calc.add(2, 2))