"""
6. **Identifying Palindromes**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, String Manipulation  
   **Description**: Write a program to check if a string or number is a palindrome.  
   **Example**:  
   Input: `string = "radar"`  
   Output: `Palindrome`  
   Explanation: "radar" reads the same backward as forward.
"""
def reverse(self, s):
    reverse_string=""
    for i in s:
        reverse_string = i+reverse_string
    if reverse_string == s:
        return "Palindrome"
    else:
        return "Not a Palindrome"
    
strings = input("Enter a String Value:") 

print(reverse(None,strings))   
