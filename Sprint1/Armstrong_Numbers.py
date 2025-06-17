lst=[]

for i in range(1,501):
    val = 0
    n=len(str(i))
    for digit in str(i):
        val+=int(digit)**n
    if val==i:
        if i==1 or i>=100:
            lst.append(val)
print(lst)