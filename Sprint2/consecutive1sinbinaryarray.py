array = [1, 1, 0, 1, 1, 1]
count=0
maxcount=0
for num in array:
    if num==1:
        count+=1
        maxcount=max(maxcount,count)
    else:
        count=0
print(maxcount)