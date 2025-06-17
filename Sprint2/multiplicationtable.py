start=2
end=4
for j in range(1, end + 1):
    for i in range(start, end + 1):
        print(i ,'x' , j ,'=',i*j,end="\t")
    print()