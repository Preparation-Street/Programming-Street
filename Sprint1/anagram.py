string1="listen"
string2="silent"
def anagram(string1,string2):
    if len(string1)!=len(string2):
        return False
    return sorted(string1)==sorted(string2)
result=anagram(string1,string2)
print(result)