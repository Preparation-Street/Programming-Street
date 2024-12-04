#find Amstrong in the give range 
def find_Amstrong(num):
    sum =0
    temp=num
    while temp>0:
        digit = temp%10
        cube = digit ** len(str(num))
        sum = sum+cube
        temp//=10
    return sum
for i in range (1,501):
    if find_Amstrong(i) == i:
        print(i)    
        
            
        