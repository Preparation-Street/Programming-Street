limit=30
count=0
def is_perfect(n):
    sumval=0
    for i in range(1,n):
        if n%i==0:
            sumval+=i
    return sumval==n
for i in range(2,limit+1):
    if is_perfect(i):
        count+=1
print(count)