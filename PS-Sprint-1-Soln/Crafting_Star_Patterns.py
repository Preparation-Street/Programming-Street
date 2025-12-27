def star_pattern(n):
    for i in range(n):
        space = " "*(n - i - 1)
        stars = "*" * (2 * i + 1   )
        
        print(space + stars)
        print()
star_pattern(5)
