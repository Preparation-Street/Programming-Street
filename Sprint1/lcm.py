a=12
b=15
maxnum=max(a,b)
while True:
    if maxnum%a==0 and maxnum%b==0:
        print(maxnum)
        break
    maxnum+=1
