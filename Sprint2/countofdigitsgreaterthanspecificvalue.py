number = 54321
value = 3
count=0
for digit in str(number):
    if int(digit)>value:
        count+=1
print(count)