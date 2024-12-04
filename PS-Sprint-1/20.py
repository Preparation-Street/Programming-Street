n = int(input(" Enter The Number : "))
divisors = []
sum = 0
for i in range(1,n):
    if n%i == 0:
        divisors.append(i)
    #print (divisors)
for d in divisors:
    sum += d
if sum == n:
    print("Number is perfect")
else:
    print("Number is not perfect")


                
        
               