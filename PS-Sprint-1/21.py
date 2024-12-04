def even_no(n):
    return n%2 ==0
sum  = 0
n= int(input(""))  
for i in range (1, n+1):
    if even_no(i):
        sum += i
print(sum)
              