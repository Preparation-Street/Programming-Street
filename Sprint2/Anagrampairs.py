strings = ["listen", "silent", "hello", "world"]
lst=[]
for i in range(len(strings)):
    for j in range(i+1,len(strings)):
        if sorted(strings[i])==sorted(strings[j]):
            lst.append((strings[i],strings[j]))
print(lst)

