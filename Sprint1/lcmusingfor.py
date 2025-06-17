a=12
b=15
maxnum=max(a,b)
for i in range(maxnum,(a*b)+1):
    if i%a==0 and i%b==0:
        print(i)
        break