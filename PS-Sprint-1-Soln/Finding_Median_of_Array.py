def med(arr):
    l = len(arr)
    arr.sort()
    if l % 2 == 0:  
        median = (arr[l // 2 - 1] + arr[l // 2]) / 2
    else:  
        median = arr[l // 2]                            
    return median   

print(med([12, 3, 5, 7, 19]))
print(med([1,2,3,4,5]))