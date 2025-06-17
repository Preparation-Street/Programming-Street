sequence=[1,2,4,5,7]
n=max(sequence)
missing_num=[]
for num in range(1,n+1):
    if num not in sequence:
        missing_num.append(num)

print(missing_num)