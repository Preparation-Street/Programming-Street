def num(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                count += 1
    return count 
print(num("abbaeae"))  # Outputs all palindromic substrings
print(num("aaa"))      # Outputs all palindromic substrings