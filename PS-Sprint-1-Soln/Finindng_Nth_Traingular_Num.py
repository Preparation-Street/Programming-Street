def Trangiular(n):
    if n == 1:
        return 1
    else:
        return n + Trangiular(n - 1)
    
print(Trangiular(5))
print(Trangiular(4))