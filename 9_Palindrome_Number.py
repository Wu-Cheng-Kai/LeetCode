def isPalindrome(x: int) -> bool:
    if x >= 0:   # 正整數才會對稱
        str_x = str(x)
        if str_x == str_x[::-1]: # 看反過來是否一樣
            return True
    return False