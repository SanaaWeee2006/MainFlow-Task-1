# 8.  Check if a number equals the sum of its digits raised to the power of the number of digits.

number = int(input("Enter the number: "))
length = len(str(number))

temp = number 
sum = 0

while temp > 0:
    digit = temp % 10 # only remainder
    sum += digit ** length
    temp = temp // 10 # no decimal

if sum == number:
    print(f"{number} is an Armstrong number!!")
else:
    print(f"{number} is not an Armstrong number!!")
    
