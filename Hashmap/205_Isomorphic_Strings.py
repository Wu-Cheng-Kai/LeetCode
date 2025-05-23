def isIsomorphic(s: str, t: str) -> bool:
    letter_s, letter_t, map = set(), set(), {}

    for i in range(len(s)):
        if s[i] in letter_s:
            if map[s[i]] != t[i]:
                return False
        elif t[i] in letter_t:
            return False
        else:
            map[s[i]] = t[i]
            letter_s.add(s[i])
            letter_t.add(t[i])

    return True

s = "ca"
t = "ab"
answer = isIsomorphic(s, t)
print(answer)