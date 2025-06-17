a=12
b=15
# lcm=a*b//gcd(a,b)
minnum=min(a,b)
for i in range(minnum,0,-1):
    if a%i==0 and b%i==0:
        gcd=i
        break
lcm=a*b//gcd
print(lcm)