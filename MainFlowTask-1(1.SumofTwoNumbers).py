# 1. Objective: Write a program to calculate the sum of two numbers. 

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter integers only.")

# number1 = 3
# number2 = 5

result = number1 + number2

print(f'The sum of {number1} and {number2} is:', result)