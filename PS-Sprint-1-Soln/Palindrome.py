def palindrome(n):
    str_1 =str(n)
    
    if str_1 == str_1[::-1] :
        print("Palindrome")
        
    else:
        print("Not a Palindrome")

print(palindrome(121))  # True
print(palindrome(123))  # False