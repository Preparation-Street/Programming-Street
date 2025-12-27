import math

def check_range(a):
    
    result = []
    for i in range(a[0],a[1]):
        x= i 
        n=0

        while (x!=0):
            x =x//10
            n =n+1

        pow_sum = 0 
        x = i
        while (x != 0) :
            digit = x % 10
            pow_sum = pow_sum + math.pow(digit, n)
            x = x//10


        if (pow_sum == i) :
            result.append(i)
        
    return result


print(check_range([1, 500]))

