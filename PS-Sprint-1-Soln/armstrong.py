def armstrong(n):
    num =str(n)
    length = len(num)
    sum = 0
    for digit in num:
        sum += int(digit) ** length 

    return sum == n

print(armstrong(153))  # True