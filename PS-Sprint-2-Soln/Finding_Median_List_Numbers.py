def median_list(list):
    sorted_list = sorted(list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        median = sorted_list[mid]
    return median
print(median_list([3, 1, 4, 2, 5]))
