def largest_Sum_array(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum
print(largest_Sum_array([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6