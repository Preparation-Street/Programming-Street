num=153
temp=num
n=len(str(num))
v=0
while (num>0):
    var=num%10
    v+=var**n
    num=num//10
if v==temp:
    print("Narcissistic Number")
else:
    print("Not")
