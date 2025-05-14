def plusOne(digits: list[int]) -> list[int]:
    num = ""
    for i in digits:     # 將list轉為數字(字串型態)
        num += str(i)
    num1 = int(num) + 1  # +1
    return list(str(num1))       # 將結果轉為字串、再轉成list