# 6. Check if a string reads the same backward as forward.

s = input("Enter the word: ")

def palindrome(s):
    return s == s[::-1]
    
result = palindrome(s)

if result:
    print("True, It's Palindrome")
else:
    print("False, it's not Palindrome")
