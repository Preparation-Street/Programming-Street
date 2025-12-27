def num(n):
    for i in range(2,n):
        if i %2 ==0:
            continue
        else:
            print(i,end=" ")

print(num(10))  # 3 5 7 9
print(num(20))  # 3 5 7 9 11 13 15 17 19