n = input("Enter the value: ")
vowel = ['a','e','i','o','u','A','E','I','O','U']
consonant = ''
vowels = ''
countV=0
countC = 0

for value in n:
    if value.isalpha():
        if value in vowel:
            vowels+=(value)
            countV +=1
        else:
            consonant+=(value)
            countC +=1
print(f"{vowels } {countV}" )
print(f"{consonant } {countC}" )
  