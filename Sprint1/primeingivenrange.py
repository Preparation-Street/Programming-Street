start=int(input("Enter a number:"))
end=int(input("Enter a number:"))
prime_number=[]
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(start,end+1):
    if is_prime(i):
        prime_number.append(i)

print(prime_number)