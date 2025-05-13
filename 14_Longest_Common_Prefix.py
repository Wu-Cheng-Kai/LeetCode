strs = ["flower","flow","flight"]

def longestCommonPrefix(strs) -> str:
    if len(strs) == 1:
        return strs[0]
    else:
        if "" not in strs:
            prefix, min_length_str = 0, 200
            for i in strs:
                if len(i) < min_length_str:
                    min_length_str = len(i)
            while prefix <= min_length_str:
                for i in range(1, len(strs)):
                    if strs[0][prefix] != strs[i][prefix]:
                        return strs[0][:prefix]
                prefix += 1
            return strs[0][:prefix]
        else:
            return ""
        
# def longestCommonPrefix(strs) -> str:
#     if len(strs) == 1:
#         return strs[0]
#     else:
#         if "" not in strs:
#             for prefix in range(200):
#                 if prefix < len(strs[0]):
#                     for i in range(1, len(strs)):
#                         if prefix >= len(strs[i]) or strs[0][prefix] != strs[i][prefix]:
#                             return strs[0][:prefix]
#                 else:
#                     return strs[0][:prefix]
#             return strs[0][:200]
#         else:
#             return ""

print(longestCommonPrefix(strs))