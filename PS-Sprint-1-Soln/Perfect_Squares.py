def squares(n):
    if n < 0:
        return 0
    else:
        for i in range(n + 1):
            if i * i == n:
                return i
            
print(squares(16))