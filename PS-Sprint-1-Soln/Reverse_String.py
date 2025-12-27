def rev(str):
    l =len(str)

    for i in range(l-1,-1,-1):
         print(str[i],end='')

     

print(rev("Hello World"))