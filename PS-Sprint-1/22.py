def odds(n):
    return n%2 != 0
sum = 0
n = int(input("Enter the number : "))
for i in range (1,n+1):
    if odds(i):
        sum +=i
print(sum)        