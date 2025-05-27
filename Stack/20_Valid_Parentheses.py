def isValid(s: str) -> bool:
    current = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for i in s:
        if i in pairs.values():
            current.append(i)
        elif current and current[-1] == pairs[i]:
            current.pop()
        else:
            return False

    return not current

s = "()[]{"
print(isValid(s))