def seq(a):
    n = len(a)
    for i in range(1, n + 1):
        if i not in a:
            return i
        
print(seq([3, 7, 1, 2, 8, 4, 5]))  # Output: 6
print(seq([1, 2,  4, 5]))        # Output: 6