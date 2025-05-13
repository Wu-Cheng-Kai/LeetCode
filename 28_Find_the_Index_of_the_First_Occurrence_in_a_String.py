# 1. simple function
# def strStr(haystack: str, needle: str) -> int:
#     return haystack.find(needle)

# 2. string matching
def strStr(haystack: str, needle: str) -> int:
    if haystack == needle:
        return 0
    else:
        h_length = len(haystack)
        n_length = len(needle)
        if h_length >= n_length > 0:
            for i in range(h_length-n_length+1):
                if needle == haystack[i:i+n_length]:
                    return i
        return -1

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))