list = [3, 1, 4, 1, 5]
list.sort()
n=len(list)
if n%2==1:
    print(list[n//2])
elif n%2==0:
    print((list[n//2-1]+list[n//2])/2)