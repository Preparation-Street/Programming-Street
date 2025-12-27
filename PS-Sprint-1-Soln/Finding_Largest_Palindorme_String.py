def plaindome(s):
    l = len(s)
    for i in range(l):
        for j in range(i + l, i, -1):
            substr = s[i:j]
            if substr == substr[::-1]:
                return substr
            

print(plaindome("babad"))  # Output: "bab" or "aba"