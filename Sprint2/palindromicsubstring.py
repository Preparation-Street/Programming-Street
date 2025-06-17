string = "aaa"
count =0
n=len(string)
for center in range(2*n-1):
    left=center//2
    right=left+(center%2)
    while left>=0 and right<n and string[left]==string[right]:
        count+=1
        right+=1
        left-=1
print(count)
