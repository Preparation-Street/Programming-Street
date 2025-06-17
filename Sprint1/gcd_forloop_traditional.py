a=48
b=18
minnum=min(a,b)
for i in range(minnum,0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break
