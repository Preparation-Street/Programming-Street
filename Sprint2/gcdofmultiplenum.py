array=[12,24,36]
res=array[0]
def compute_gcd(a,b):
    while b!=0:
        c=a%b
        a=b
        b=c
    return a
for num in array[1:]:
    res=compute_gcd(res,num)
print(res)

