# 3. Compute the factorial of a given number

num = int(input("Enter the number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f'The factorial of {num} is', factorial)
    
# using recursive function

n = int(input("Enter the number: "))

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(f'Factorial of {n} using recursive method is', fact(n))
