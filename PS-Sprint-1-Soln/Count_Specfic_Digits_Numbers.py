def count(n,d):
    count = 0
    s1= str(n).split(',')
    for i in s1:
        count += str(i).count(str(d))
    return count

print(count(125,2))
print(count(123456,3))
