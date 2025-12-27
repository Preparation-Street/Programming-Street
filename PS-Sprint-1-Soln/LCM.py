def LCM(a,b):
    if b==0:
        return a
    else:
        return LCM(b, a%b)
    
print(LCM(4,5))  # Output: 20
print(LCM(6,8))  # Output: 24