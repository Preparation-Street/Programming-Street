a=48
b=18
if b>a:
    a,b=b,a
while a>b and a%b!=0:
    c=a%b
    a=b
    b=c
print(c)