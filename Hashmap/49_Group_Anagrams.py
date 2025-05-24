def groupAnagrams(strs: list) -> list:
    group = []
    word = {}

    for i in strs:
        s_sort = "".join(sorted(i))
        if s_sort in word:
            group[word[s_sort]].append(i)
        else:
            group.append([i])
            word[s_sort] = len(group) - 1

    return group

strs = ["stop","pots","reed","","tops","deer","opts",""]
answer = groupAnagrams(strs)
print(answer)
