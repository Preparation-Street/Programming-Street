n=5
res=0
i=1
lst=[]
while res<n:
    if i%2!=0:
        lst.append(i)
        res+=1
    i+=1
print(sum(lst))




