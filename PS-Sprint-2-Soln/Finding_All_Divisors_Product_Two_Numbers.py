def Divisors_Product(num1 , num2):
    product = num1 * num2
    divisors = []
    for i in range(1, product//2 ):
        if product % i == 0 and i%4!=0:
            divisors.append(i)
    return divisors
    
          

print(Divisors_Product(4, 6))
print(Divisors_Product(6, 10))