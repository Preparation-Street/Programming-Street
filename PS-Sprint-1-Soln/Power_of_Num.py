def pow_Num(b ,e):
    if e == 0:
        return 1
    elif e < 0:
        return 1 / pow_Num(b, -e)
    else:
        return b * pow_Num(b, e - 1)
print(pow_Num(2, 3))
