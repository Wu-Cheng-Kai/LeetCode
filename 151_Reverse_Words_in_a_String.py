# def reverseWords(s: str) -> str:
#     reverse = ""
#     for i in s.split():
#         reverse = i + " " + reverse
#     return reverse[:-1]

def reverseWords(s: str) -> str:
    return " ".join(list(reversed(s.split())))

s = "the sky is blue"
print(reverseWords(s))