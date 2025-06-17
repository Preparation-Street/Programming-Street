number=9875
def sumofdigits(number):
    temp = 0
    if number<=9:
        return number
    while (number > 0):
        val = number % 10
        temp = temp + val
        number = number // 10
    return sumofdigits(temp)

result=sumofdigits(number)
print(result)
