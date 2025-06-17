start=1
end=100
result=[]
for num in range(start,end+1):
    if str(num)==str(num)[::-1]:
        result.append(num)
print(result)