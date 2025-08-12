# A simple calculator class to perform basic arithmetic operations.
class Calculator:

    def __init__(self, a, b):
        self.a = a  
        self.b = b  

    def add(self):
        return self.a + self.b

    
    def subtract(self):
        return self.a - self.b

    
    def multiply(self):
        return self.a * self.b


    def divide(self):
        
        if self.b == 0:
            return "Error: Cannot divide by zero!"
        else:
            return self.a / self.b


number_a = 15
number_b = 40
operation = "addition" 


my_calculator = Calculator(number_a, number_b)

if operation == "addition":
    result = my_calculator.add()
elif operation == "subtraction":
    result = my_calculator.subtract()
elif operation == "multiplication":
    result = my_calculator.multiply()
elif operation == "division":
    result = my_calculator.divide()
else:
    result = "Error: Invalid operation specified."

# results
print(f"The result of {number_a} {operation} with {number_b} is: {result}")
