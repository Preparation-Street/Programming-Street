arr=[3,1,4,1,5,9]

for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)


