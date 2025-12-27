def longest_consecutive_sequence(arr):
    if not arr:
        return 0

    num_set = set(arr)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start of a new sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # Output: 4