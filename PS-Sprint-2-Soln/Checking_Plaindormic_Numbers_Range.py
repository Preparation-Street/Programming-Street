def Checking_Plaindormic_Numbers_Range(start, end):
    palindromic_numbers = []
    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            palindromic_numbers.append(num)
    return palindromic_numbers

print(Checking_Plaindormic_Numbers_Range(1, 100))