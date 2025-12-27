def multipication(a,b):
    """Generate multiplication table from a to b (inclusive)."""
    for i in range(a, b + 1):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()  # Print a blank line after each table

print(multipication(3,5))