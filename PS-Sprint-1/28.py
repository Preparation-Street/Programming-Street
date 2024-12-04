def fact(n):
    
    if n ==1 or n== 0:
        return 1
    for i in range (2,n):
        n*=i
    return n
n = int(input(""))
(fact(n))
sum = 0
no = fact(n)
while no>0:
    digit = no%10
    sum += digit
    no= no//10
    
print(sum)        
        