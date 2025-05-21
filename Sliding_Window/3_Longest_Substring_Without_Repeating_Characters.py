s = 'aabaab!bb'
# print(s[1])

word = []
word_len, max_len = 0, 0

for i in range(len(s)):
    if s[i] not in word:
        word.append(s[i])
        word_len += 1
    else:
        idx = word.index(s[i])
        word = word[idx+1:]
        word.append(s[i])
        word_len -= idx
        
    if word_len > max_len:
        max_len = word_len
    print(word, max_len, word_len)

print(max_len)