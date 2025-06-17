string = "abcabcbb"
charset=set()
longest=0
n=len(string)
s=0
l=0
start=0
for r in range(n):
    if string[r] in charset:
        charset.remove(string[l])
        l+=1
    charset.add(string[r])
    w=r-l+1
    if w>longest:
        longest=w
        start=l
print(string[start:start+longest])