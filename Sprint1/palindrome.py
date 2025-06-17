s=input("Enter a string")
s=s.lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not")
