def GCD(n1, n2):
    if n2 == 0:
        return n1
    else:
        return GCD(n2, n1 % n2)
    
print(GCD(48, 18))  # Output: 6
print(GCD(32,16))  # Out