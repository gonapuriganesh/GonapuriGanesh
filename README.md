Project Name: Gonapuri Ganesh
File Names: Problem-1, Problem-2, Problem-3, Problem-4
Coding Language: Python

> problem-1
Simple  Calculator
This project is a straightforward example of a basic calculator implemented as a Python class. It's designed to perform basic arithmetic operations like addition, subtraction, multiplication, and division—on two numbers.

The Code:
#A simple calculator class to perform basic arithmetic operations.

class Calculator:
"""
This class can perform addition, subtraction, multiplication, and division
on two numbers.
"""

#The constructor method, which initializes the object with two numbers.
def __init__(self, a, b):
    self.a = a # Stores the first number
    self.b = b  # Store the second number

#Method to add the two numbers.
def add(self):
    return self.a + self.b

#Method to subtract the second number from the first.
def subtract(self):
    return self.a - self.b

#Method to multiply the two numbers.
def multiply(self):
    return self.a * self.b

#Method to divide the two numbers, with a check for division by zero.
def divide(self):
    if self.b == 0:
        return "Error: Cannot divide by zero!"
    else:
        return self.a / self.b

        
number_a = 15
number_b = 40
operation = "addition"

#Create a new Calculator object with the numbers.
my_calculator = Calculator(number_a, number_b)

Perform the selected operation and get the result.
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

#Print the final result.
print(f"The result of {number_a} {operation} with {number_b} is: {result}")


> problem-2

Odd Number Series Generator
This project is a simple Python script designed to generate a series of odd numbers. By providing a single integer as input, the script will produce a comma-separated string containing the first n odd numbers, where n is your input.

The Code
#Odd Number Series Generator class
def generate_odd_series(number):
   odd_numbers=[]
#using for loop
   for i in range(1,2*number,2):
		odd_numbers.append(str(i))

 return ", ".join(odd_numbers)


num = 3
output = generate_odd_series(num)
print(f"input a = {num}, then output: {output}")

Example Input and Output
Input:
num = 4
Output:
input a = 3, then output: 1, 3, 5

> problem-3
Conditional Odd Number Series Generator
This project is a Python script that generates a series of odd numbers based on a unique condition related to the input integer.

#If the input number is odd, It generates a series containing that exact number of odd terms.

$If the input number is even, It generates a series with one less term than the input number.


The Code
def generate_condtional_odd_series(a):

   if a % 2 != 0:
       limit = a
     else:
       limit = a - 1

   odd_numbers = [str(i) for i in range(1, 2 * limit, 2)]
     return ",".join(odd_numbers)

num=5
output=generate_condtional_odd_series(num)
print(f" input a={num} then output is {output}")

Example Input and Output
Input:
num = 5

Output:
input a=5 then output is 1,3,5,7,9

> problem-4
Multiple Counter
This project is a Python script that counts the occurrences of multiples for each number from 1 to 9 within a given list. It provides a clear and organized way to analyze a list of numbers and understand their divisibility.

Getting Started
To use this script, copy the code below into a Python file (e.g., multiple_counter.py). You can then execute it from your terminal.

python multiple_counter.py

Feel free to modify the input_list to test the functionality with your own set of numbers.

The Code:
def count_multiples(numbers):
  
  #Counts how many numbers in a given list are multiples of each number from 1 to 9.

  #Initialize an empty dictionary to store the counts.
  multiples_counts = {}

  #Check for multiples of numbers from 1 to 9.
  for divisor in range(1, 10):
        # Reset the counter for each new divisor.
        count = 0
        # Check each number in the input list.
        for number in numbers:
            # If the number is a multiple of the current divisor, increment the count.
            if number % divisor == 0:
                count += 1
        # After checking all numbers, store the final count in the dictionary.
        multiples_counts[divisor] = count
    return multiples_counts


input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output_counts = count_multiples(input_list)

print(f"input: {input_list}")
print(f"Output:")
print(f"  {output_counts}")

Example Input and Output
Input List:
[1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

Output Dictionary:
{1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
