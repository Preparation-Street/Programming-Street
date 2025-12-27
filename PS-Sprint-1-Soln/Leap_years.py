def leap_years(n):
    if n % 4 == 0:
        return True
    else:
        return False

print(leap_years(2020))  # True
print(leap_years(2019))  # False