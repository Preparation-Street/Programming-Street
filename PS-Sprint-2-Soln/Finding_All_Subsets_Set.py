def Subsets(set):
    result = []

    for i in range(2 ** len(set)):
        subset = []
        for j in range(len(set)):
            if (i & (1 << j)) > 0:
                subset.append(set[j])
        result.append(subset)
    return result
print(Subsets([1, 2]))
print(Subsets(['a', 'b']))