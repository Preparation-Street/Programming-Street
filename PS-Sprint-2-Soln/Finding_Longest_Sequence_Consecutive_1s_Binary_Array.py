def longest_Sequnce(arr):
    max_count = 0
    current_count = 0

    for num in arr:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count
print(longest_Sequnce([1, 1, 0, 1, 1, 1]))