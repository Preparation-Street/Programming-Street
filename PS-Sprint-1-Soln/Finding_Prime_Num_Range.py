def range_prime(a):
    result =[]
    for i in range(a[0],a[1]):
        if i>1:
            if i %2==0:
                pass
            else:
                result.append(i)
    return result
print(range_prime([10,50]))
print(range_prime([10,30]))