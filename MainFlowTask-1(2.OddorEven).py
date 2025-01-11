# 2. Determine whether a number is odd or even.. 

# number = int(input("Enter the number: "))
try:
    number = int(input("Enter the number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# number = 34

if number % 2 == 0:
    print("Even")
else:
    print("Odd")