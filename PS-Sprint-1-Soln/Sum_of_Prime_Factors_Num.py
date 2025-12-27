def Sum_Of_Prime_Factors_Num(n):
    for i in range(2, n + 1):
        if n % i == 0 and prime(i):
            n = n // i
            yield i
            break   
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 


print(sum(Sum_Of_Prime_Factors_Num(12)))
print(sum(Sum_Of_Prime_Factors_Num(15)))