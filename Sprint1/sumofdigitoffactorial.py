num=4
fact=1
for i in range(1,num+1):
    fact=fact*i
sumval=0
while(fact>0):
    v=fact%10
    sumval+=v
    fact=fact//10
print(sumval)