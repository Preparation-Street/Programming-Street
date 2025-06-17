array=[1,2,3,4,5,6]
even=0
odd=0
for num in array:
    if num%2==0:
        even+=num
    else:
        odd+=num
print(even-odd)
