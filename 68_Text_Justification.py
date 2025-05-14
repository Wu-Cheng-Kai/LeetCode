def fullJustify(words, maxWidth: int):
    full_s, row_s = [], ""
    current_length, current = 0, []
    for i in range(len(words)):
        word_length = len(words[i])
        if current_length + word_length > maxWidth:
            row_num = len(current)
            remain = maxWidth - current_length + row_num
            if row_num == 1:
                row_s = current[0] + " " * remain
            else:
                space_min = remain // (row_num - 1)
                r = remain % (row_num - 1)    
                for j in range(row_num-1):
                    space = space_min + 1 if j < r else space_min
                    current.insert(2 * j + 1, " " * space)
                    row_s = "".join(current)

            full_s.append(row_s)
            row_s, current_length, current = "", 0, []

        current.append(words[i])
        current_length += word_length + 1

    remain = maxWidth - current_length + 1
    full_s.append(" ".join(current) + " " * remain)

    return full_s

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 16

print(fullJustify(words, maxWidth))