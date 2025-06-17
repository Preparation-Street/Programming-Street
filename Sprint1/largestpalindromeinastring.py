def is_palindrome(s):
    return s==s[::-1]
def find_longest_palindrome(s):
    longest=""
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            part=s[i:j]
            if is_palindrome(part) and len(part)>len(longest):
                longest=part
    return longest
s='ababa'
result=find_longest_palindrome(s)
print(result)