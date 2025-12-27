def checking_anagram_pairs(list_of_strings):
    anagram_pairs = []
    n = len(list_of_strings)
    for i in range(n):
        for j in range(i + 1, n):
            if sorted(list_of_strings[i]) == sorted(list_of_strings[j]):
                anagram_pairs.append((list_of_strings[i], list_of_strings[j]))
    return anagram_pairs
print(checking_anagram_pairs(["listen", "silent", "enlist", "hello", "world", "dlorw"]))
