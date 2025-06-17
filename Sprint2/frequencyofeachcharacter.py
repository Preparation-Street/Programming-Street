string = "hello"
hash_set={}
for s in string:
    if s not in hash_set:
        hash_set[s]=1
    elif s in hash_set:
        hash_set[s]+=1
print(hash_set)