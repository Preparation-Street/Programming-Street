number=123
def sumofdigitsuntilzero(number):
    num=0
    if number<=9:
        return number
    while number>0:
        var=number%10
        num=num+var
        number=number//10
    return sumofdigitsuntilzero(num)

print(sumofdigitsuntilzero(number))