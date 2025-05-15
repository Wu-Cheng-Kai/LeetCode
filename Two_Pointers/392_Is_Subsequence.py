def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    elif len(t) > 0:
        for char in t:
            if char == s[0]:
                if len(s) == 1:
                    return True
                else:
                    s = s[1:]
    return False
    

s = "abrc"
t = "ahbgdc"

print(isSubsequence(s, t))