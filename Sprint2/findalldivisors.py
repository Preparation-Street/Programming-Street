number1 = 6
number2 = 10
product=number1*number2
def get_divisors(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)

    return lst
res=get_divisors(product)
print(res)