def narcissistic(n):
    if n % 10 ** 3 == (n // 100) ** 3 + ((n // 10) % 10) ** 3 + (n % 10) ** 3:
        return "Narcissistic Number"
    else:
        return "Not a Narcissistic Number"
    
print(narcissistic(153))  # Narcissistic Number
print(narcissistic(123))  # Not a Narcissistic Number