array = [-1, 0, 1, 2, -1, -4]
lst=[]
for i in range(len(array)):
    for j in range(i+1,len(array)):
        for k in range(j+1,len(array)):
            triplet=sorted([array[i],array[j],array[k]])
            if sum(triplet)==0 and triplet not in lst:
                lst.append(triplet)
print(lst)


