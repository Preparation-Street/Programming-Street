def arr(a):
    a.sort()
    return a[-2]

print(arr([1,2,3,4,5]))
print(arr([10,20,5,15,25]))