def findSubstring(s: str, words: list):
    word_len = len(words[0])
    max_len = word_len * len(words)
    find, history = [], set()
    word_check = words.copy()

    for i in range(len(s)-max_len+1):
        s_slice = s[i:i+max_len]
        if s_slice not in history:
            for j in range(len(words)):
                word = s_slice[j*word_len:j*word_len+word_len]
                # print(s_slice, word, word_check)
                if word in word_check:
                    word_check.remove(word)
                else:
                    break
            if not word_check:
                find.append(i)
                history.add(s_slice)
            word_check = words.copy()
        else:
            find.append(i)

    return find

s = "barfoothefoobarman"
words = ["foo","bar"]

ans = findSubstring(s, words)
print(ans)