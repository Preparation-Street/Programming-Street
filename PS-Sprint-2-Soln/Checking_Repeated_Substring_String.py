def repeated_String(str):
    n = len(str)
    for i in range(1, n//2 + 1):
        if n % i == 0:
            substring = str[:i]
            if substring * (n // i) == str:
                return True
    return False
print(repeated_String("abab"))