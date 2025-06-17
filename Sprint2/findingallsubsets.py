set=[1,2]
def subset(nums):
    result=[[]]
    for num in nums:
        new_subset=[]
        for subset in result:
            new_subset.append(subset+[num])
        result+=new_subset
    return result
print(subset(set))