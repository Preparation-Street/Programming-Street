def Mode(a):
    for i in a:
        if a.count(i) > 1:
            return i
    return -1

print(Mode([1,2,3,3,4,5]))
print(Mode([1,2,3,4,5]))