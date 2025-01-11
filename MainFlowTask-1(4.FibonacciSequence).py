# 4.Generate the first nnn numbers in the Fibonacci sequence.

num = int(input("Enter the number of terms: "))

n1, n2 = 0, 1
count = 0 

if num < 0:
    print("Invalid Input !!")
elif num == 1:
    print("Fibonacci Series: ", n1)
else:
    while count < num: 
        print(n1) 
        term = n1 + n2  
        n1 = n2 
        n2 = term 
        count += 1  