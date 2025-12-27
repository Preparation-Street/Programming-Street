def Counting(str):
    l = len(str)

    vcount = 0
    ccount = 0
    for i in range(l):
        if str[i] in 'aeiouAEIOU':
            vcount = vcount + 1
        elif (str[i] >= 'a' and str[i] <= 'z') or (str[i] >= 'A' and str[i] <= 'Z'):
            ccount = ccount + 1
        
    return print("Vowels:", vcount, "Consonants:", ccount)


print(Counting("Hello World"))  # Output: Vowels: 3 Consonants: 7
print(Counting("Programming Street"))  # Output: Vowels: 5 Consonants