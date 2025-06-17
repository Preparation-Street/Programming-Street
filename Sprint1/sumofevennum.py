start=int(input("Enter a starting number:"))
end=int(input("Enter a ending number:"))
lst=[]
for i in range(start,end+1):
    if i%2==0:
        lst.append(i)
print(sum(lst))
