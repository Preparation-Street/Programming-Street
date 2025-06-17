string="The numbers are 12 and 34"
total=0
num=''
for char in string:
    if char.isdigit():
        num+=char
    else:
        if num!='':
            total+=int(num)
            num=''
if num!='':
    total+=int(num)
print(total)