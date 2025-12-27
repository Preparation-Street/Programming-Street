def patterns(n):
    cur_num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(cur_num, end=" ")
            cur_num += 1
        print()

print(patterns(3))