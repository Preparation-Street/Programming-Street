string = "{[()]}"
def is_balanced(string):
    stack=[]
    bracket_map={')':'(','}':'{',']':'['}
    for char in string:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop()!=bracket_map[char]:
                return False
    return not stack
print(is_balanced(string))