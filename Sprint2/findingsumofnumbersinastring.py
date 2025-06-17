import re
string="The numbers are 12 and 34"
numbers=re.findall(r'\d+',string)
print(sum(map(int,numbers)))