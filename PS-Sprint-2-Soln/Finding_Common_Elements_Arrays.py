def common_elements(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    common = set1.intersection(set2)
    return list(common)
arr1 = [1,2,3,4,5,6]
arr2 = [4,5,6,7,8,9]    
print(common_elements(arr1,arr2))