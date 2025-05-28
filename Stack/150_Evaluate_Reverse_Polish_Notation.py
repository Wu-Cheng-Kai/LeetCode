def evalRPN(tokens: list) -> int:
    nums = []

    for i in tokens:
        if i == "+":
            nums[-1] = nums[-2] + nums.pop()
        elif i == "-":
            nums[-1] = nums[-2] - nums.pop()
        elif i == "*":
            nums[-1] = nums[-2] * nums.pop()
        elif i == "/":
            nums[-1] = int(nums[-2] / nums.pop())
        else:
            nums.append(int(i))

    return nums[0]

def evalRPN1(tokens: list) -> int:
    nums = []
    operator = {
        "+" : lambda a, b : a + b,
        "-" : lambda a, b : a - b,
        "*" : lambda a, b : a * b,
        "/" : lambda a, b : int(a / b)
    }

    for i in tokens:
        if i in operator.keys():
            nums[-1] = operator[i](nums[-2], nums.pop())
        else:
            nums.append(int(i))

    return nums[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN1(tokens))