n=4
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
res=0
i=2
sum=0
while(res<n):
    if is_prime(i):
        res+=1
        sum+=i
    i+=1
print(sum)

