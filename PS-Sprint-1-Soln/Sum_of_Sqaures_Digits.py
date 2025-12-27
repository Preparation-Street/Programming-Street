def sum_of_Squares(n):
    count = 0 
    for i in range(len(str(n))):
        digit = n % 10
        count += digit * digit
        n = n // 10
    return count

print(sum_of_Squares(123))
print(sum_of_Squares(456))