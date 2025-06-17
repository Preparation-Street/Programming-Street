number=28

lst=[]
def is_prime(number):
    count = 0
    for i in range(2,number):
        if number%i==0:
            return False
    return True

for i in range(2,number+1):
    if number%i==0:
        if is_prime(i):
            lst.append(i)
print(max(lst))
