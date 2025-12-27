def longest_unique_substring(s):
    # 1. Change char_Set to a Set!
    char_Set = set() # <--- FIXED
    max_Length = 0
    left = 0

    for right in range(len(s)):
        while s[right] in char_Set:
            # 2. Use .remove() instead of .replace()
            char_Set.remove(s[left]) # <--- FIXED
            left += 1

        # 3. Use .add() instead of string concatenation
        char_Set.add(s[right]) # <--- FIXED
        max_Length = max(max_Length, right - left + 1) 

    return max_Length
print(longest_unique_substring("abcabcbb"))  # Output: 3