def balance(str):
    if len(str) % 2 != 0:
        return False
    else:
        for i in range(len(str)//2):
            if str[i] == '(' and str[len(str)-1-i] != ')':
                return False
            elif str[i] == '{' and str[len(str)-1-i] != '}':
                return False
            elif str[i] == '[' and str[len(str)-1-i] != ']':
                return False

        return True

print(balance("({[]})"))
print(balance("((()))"))