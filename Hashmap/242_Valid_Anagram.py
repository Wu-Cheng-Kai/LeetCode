def isAnagram(s: str, t: str) -> bool:
    s_set, t_set = set(s), set(t)
    
    if s_set != t_set:
        return False
    else:
        for i in s_set:
            if s.count(i) != t.count(i):
                return False

    return True

def isAnagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    else:
        letter, map = set(), {}
        for i in range(len(s)):
            if s[i] in letter:
                map[s[i]] += 1
            else:
                map[s[i]] = 1
                letter.add(s[i])
            if t[i] in letter:
                map[t[i]] -= 1
            else:
                map[t[i]] = -1
                letter.add(t[i])

    return max(map.values()) == 0 and min(map.values()) == 0



s = "anagram"
t = "nagaram"
answer = isAnagram1(s, t)
print(answer)