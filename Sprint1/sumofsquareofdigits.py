number=123
squareval=0
while (number>0):
    val=number%10
    squareval+=val**2
    number=number//10
print(squareval)