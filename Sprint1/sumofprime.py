number=12
lst=[]
def is_prime(number):
    if number<=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
for i in range(2,number+1):
    if is_prime(i) and number%i==0:
        lst.append(i)
print(sum(lst))
