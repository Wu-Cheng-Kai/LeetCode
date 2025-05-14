def romanToInt(s: str) -> int:
    dict1 = {'I' : 1,
             'V' : 5,
             'X' : 10,
             'L' : 50,
             'C' : 100,
             'D' : 500,
             'M' : 1000}

    dict2 = {'IV' : 4,
             'IX' : 9,
             'XL' : 40,
             'XC' : 90,
             'CD' : 400,
             'CM' : 900}

    sum = 0
    sp = len(s)
    while sp > 0:
        if sp > 1:                        # 從尾巴搜尋，先搜尋兩個字，如果沒有才會搜尋一個字
            if s[sp-2:sp] in dict2:
                sum += dict2[s[sp-2:sp]]
                sp -= 2
                continue

        sum += dict1[s[sp-1]]
        sp -= 1

    return sum

def romanToInt1(s: str) -> int:
    dict = {'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000}
    
    s = s.replace('IV', 'IIII')
    s = s.replace('IX', 'VIIII')
    s = s.replace('XL', 'XXXX')
    s = s.replace('XC', 'LXXXX')
    s = s.replace('CD', 'CCCC')
    s = s.replace('CM', 'DCCCC')

    integer = 0
    for i in s:
        integer += dict[i]

    return integer

s = "MCMXCIV"
output = romanToInt1(s)
print(output)