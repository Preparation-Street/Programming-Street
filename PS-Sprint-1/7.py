"""
7. **Crafting Star Patterns**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Patterns  
   **Description**: Write a program to create different star patterns (e.g., pyramid, diamond).  
   **Example**:  
   Input: `patternType = "pyramid", height = 5`  
   Output:  
   ```
       *
      ***
     *****
    *******
   *********
   ```  
   Explanation: A pyramid pattern with a height of 5 is generated.
"""
n = int(input("Enter the height of the pyramid: "))
for i in range (n):
    for j in range (n-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    for l in range(n-i-1):
        print(" ", end="")
    print()                
