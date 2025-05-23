def canConstruct(ransomNote: str, magazine: str) -> bool:
    letter = set()

    for s in ransomNote:
        if s not in letter:
            if ransomNote.count(s) > magazine.count(s):
                return False
            else:
                letter.add(s)
        
    return True

def canConstruct1(ransomNote: str, magazine: str) -> bool:
    letter = set(ransomNote)

    for s in letter:
        if ransomNote.count(s) > magazine.count(s):
            return False
            
    return True

ransomNote = "aab"
magazine = "baa"

answer = canConstruct(ransomNote, magazine)
print(answer)
