def sum_Prime(a):
    count  = 0 
    
    for i in range(a[0] +1 ,a[-1]+1):
        if prime(i):
            count += i
        else:
            continue
    return count


def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(sum_Prime([10,30]))
print(sum_Prime([1,10]))