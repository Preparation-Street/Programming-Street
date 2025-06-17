number1=12
number2=34
product=number1*number2
print(product)
sumval=0
while product:
    val=product%10
    sumval=sumval+val
    product=product//10
print(sumval)