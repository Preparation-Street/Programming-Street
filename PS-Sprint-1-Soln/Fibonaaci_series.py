def feb(n):
    for i in range(n):
        if i == 0:
            print(0, end=" ")
        elif i == 1:
            print(1, end=" ")
        else:
            a, b = 0, 1
            for j in range(2, i + 1):
                c = a + b
                a = b
                b = c

            if b<=n:
                    print(b, end=" ")

            else:
                    break

print(feb(10))  # 0 1 1 2 3 5 8 13 21 34