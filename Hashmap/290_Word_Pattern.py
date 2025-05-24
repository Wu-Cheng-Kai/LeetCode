def wordPattern(pattern: str, s: str) -> bool:
    letter, words, map = set(), set(), {}
    s = s.split()

    if len(pattern) != len(s):
        return False
    else:
        for i in range(len(pattern)):
            print(pattern[i], s[i])
            if pattern[i] in letter:
                if map[pattern[i]] != s[i]:
                    return False
            elif s[i] in words:
                return False
            else:
                map[pattern[i]] = s[i]
                letter.add(pattern[i])
                words.add(s[i])

        return True

pattern = "abba"
s = "dog cat cat fish"
answer = wordPattern(pattern, s)
print(answer)