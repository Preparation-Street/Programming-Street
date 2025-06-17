array = [100, 4, 200, 1, 3, 2,201,300,202,400,203,400,204]
def longest_consequence(nums):
    if not nums:
        return 0
    nums.sort()
    max_length=1
    current_length=1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            continue
        elif nums[i]==nums[i-1]+1:
            current_length+=1
        else:
            max_length=max(max_length,current_length)
            current_length=1
    max_length=max(max_length,current_length)
    return max_length


print(longest_consequence(array))