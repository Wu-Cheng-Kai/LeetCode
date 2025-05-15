# 1. check reversed
# def isPalindrome(s: str) -> bool:
#     if len(s) == 1:
#         return True
#     else:
#         s = s.lower().replace(" ", "")
#         for i in s:
#             if not i.isalnum():
#                 s = s.replace(i, "")
#         return s == s[::-1]

# 2. 
def isPalindrome(s: str) -> bool:
    if len(s) == 1:
        return True
    else:
        s_modify = ""
        for i in s:
            if i.isalnum():
                s_modify += i.lower()

        for j in range(len(s_modify)//2):
            if s_modify[j] != s_modify[-j-1]:
                return False
            
        return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))