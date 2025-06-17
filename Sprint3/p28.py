n=4
for i in range(n):
    ch=chr(65+i)
    if i==0:
        print(ch)
    else:
        print(ch,end="")
        print(" "*(2*i-1),end="")
        print(ch)

