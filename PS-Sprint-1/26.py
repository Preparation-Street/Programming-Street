def Narcissistic(n):
    temp = n
    sum = 0
    while temp >0:
        digit =temp % 10
        sum = sum + digit ** len(str(n))
        temp = temp //10
        
    if sum == n:
        print(f"{"Number is Narcissistic"}")
    else:
        print(f"{"Number is not Narcissistic"}")    
n = int (input("Enter a number"))
(Narcissistic(n))            
        