def pair_elements(arr , target):
    pairs = []
    seen = set()
    for i in arr:
        check = target - i
        if check in seen:
            pairs.append((check, i))
        seen.add(i)
    return pairs

print(pair_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))  # Output: [(1, 9), (2, 8), (3, 7), (4, 6)]