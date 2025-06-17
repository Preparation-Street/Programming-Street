string = "hello world"
vowels="aeiouAEIOU"
vowel=0
consonant=0
for char in string:
    if char.isalpha():
        if char in vowels:
            vowel+=1
        else:
            consonant+=1
print(vowel,consonant)
