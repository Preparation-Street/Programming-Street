string1="listen"
string2="silent"
def anagram(string1,string2):
    if len(string1)!=len(string2):
        return False
    count1={}
    for char in string1:
        count1[char]=count1.get(char,0)+1
    for char in string2:
        if char not in count1:
            return False
        count1[char]-=1
        if count1[char]<0:
            return False
    return all(value == 0 for value in count1.values())
result=anagram(string1,string2)
print(result)