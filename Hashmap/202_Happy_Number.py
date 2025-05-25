def isHappy(n: int) -> bool:
    history = set()
    square = {
        '0' : 0,
        '1' : 1,
        '2' : 4,
        '3' : 9,
        '4' : 16,
        '5' : 25,
        '6' : 36,
        '7' : 49,
        '8' : 64,
        '9' : 81
    }

    while n != 1:
        if n in history:
            return False
        else:
            s = 0
            history.add(n)
            for i in str(n):
                s += square[i]
            n = s

    return True

def isHappy1(n: int) -> bool:
    history = set()

    while n != 1:
        if n in history:
            return False
        else:
            s = 0
            history.add(n)
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            n = s

    return True

n = 19
print(isHappy1(n))