number = 122333
digit=3
count=0
while(number>0):
    val=number%10
    if val==digit:
        count+=1
    number//=10
print(count)
