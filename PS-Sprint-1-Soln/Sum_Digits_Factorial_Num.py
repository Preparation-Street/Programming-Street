def num(n):
        if n ==1 or n==0:
            return 1
        else:
            return n * num(n-1)
    
def sum(n):
     n1 = num(n)
     s1 = str(n1)
     sum1  = 0
     for i in s1:
         sum1 = sum1 + int(i)
     return sum1


print(sum(5))  # Output: 3
print(sum(4)) # Output: 27
    
   
        
    