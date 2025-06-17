number=int(input("Enter a number"))
temp=number
numdig=len(str(number))
val=0
while number>0:
    n=number%10
    val=val+n**numdig
    number=number//10
if val==temp:
    print("Armstrong")
else:
    print("Not")