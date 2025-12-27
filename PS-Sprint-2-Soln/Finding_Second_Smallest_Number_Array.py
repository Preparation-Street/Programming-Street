def second_smallest(arr):
    first = second = float('inf')
    for number in arr:
        if number < first:
            second = first
            first = number
        elif first < number < second:
            second = number
    return second if second != float('inf') else None

print(second_smallest([12, 3, 5, 7, 19]))
print(second_smallest([1, 2, 2, 1]))    