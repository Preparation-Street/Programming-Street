array=[1,2,3,4,5]
target=5
lst=[]
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]+array[j]==target:
            lst.append((array[i],array[j]))
print(lst)
