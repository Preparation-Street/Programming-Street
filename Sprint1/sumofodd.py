start=int(input("Enter a starting number:"))
end=int(input("Enter a ending number:"))
sumval=0
for i in range(start,end+1):
    if i%2!=0:
        sumval+=i
print(sumval)
