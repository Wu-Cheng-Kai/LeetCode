num = 3749

# # 1. 
# roman = ""

# dict1 = {'M' : 1000,
#          'CM' : 900,
#          'D' : 500,
#          'CD' : 400,
#          'C' : 100,
#          'XC' : 90,
#          'L' : 50,
#          'XL' : 40,
#          'X' : 10,
#          'IX' : 9,
#          'V' : 5,
#          'IV' : 4,
#          'I' : 1}

# for i in dict1:
#     roman += i * (num // dict1[i])
#     num %= dict1[i]

# 2.
thousand = ["", "M", "MM", "MMM"]
hundred = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
one = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

roman = thousand[num//1000] + hundred[(num%1000)//100] + ten[(num%100)//10] + one[(num%10)]

print(roman)