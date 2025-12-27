def len1(s):
    for i in s:
        count = 0
        for j in s:
            count += 1
        return count
print(len1("Hello"))
print(len1("Programming Street"))