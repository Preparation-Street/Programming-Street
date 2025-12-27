def longest_String(str1):
    words = str1.split()
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest
print(longest_String("I am learning Python programming"))  # Output: 11