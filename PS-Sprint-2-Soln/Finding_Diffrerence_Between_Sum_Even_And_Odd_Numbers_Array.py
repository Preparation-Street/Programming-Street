def diffrence_between_sum_even_odd(arr):
    sum_even = 0
    sum_odd = 0
    
    for num in arr:
        if num == 1:
            continue
        elif num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
            
    return abs(sum_even - sum_odd)
print(diffrence_between_sum_even_odd([1, 2, 3, 4, 5, 6]))  # Output: 3