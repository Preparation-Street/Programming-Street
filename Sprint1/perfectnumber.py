num=28
lst=[]
for i in range(1,num):
    if num%i==0:
        lst.append(i)

if sum(lst)==num:
    print("Perfect")
else:
    print("Not perfect")
