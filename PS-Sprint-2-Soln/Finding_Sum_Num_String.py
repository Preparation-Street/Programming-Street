def Sum_Num_String(s):
    total = 0
    current_number = ""
    for char in s:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                total += int(current_number)
                current_number = ""
    if current_number:
        total += int(current_number)

    return total    

print(Sum_Num_String("abc123"))
print(Sum_Num_String("1a2b3c4d5e"))
print(Sum_Num_String("The numbers are 12 and 34"))