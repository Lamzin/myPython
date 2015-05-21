#! usr/bin/env python3.4
import time
time_beg = time.time()

prior = {"(": 1, ")": 1, "+": 2, "-": 2, "*": 3, "/": 3, "^": 3}
operations = ["+", "-", "*", "/", "^"]
function = {"+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: a/b,
            "^": lambda a, b: a**b}

def rpn(string):
    stack, oper, cur_num, bnum, sign, string = [], [], 0, False, 1, "(" + string + ")"

    for i, ch in enumerate(string):
        if ord(ch) in range(48, 58):
            cur_num, bnum = cur_num * 10 + ord(ch) - 48, True
        elif ch != " " and ch != "\n":
            if bnum:
                stack.append(cur_num * sign)
                cur_num, bnum, sign = 0, False, 1
            if (ch == "+" or ch == "-") and i and string[i-1] == "(":
                if ch == "-":
                    sign *= -1
            elif ch in operations:
                while oper and prior[oper[-1]] >= prior[ch]:
                    stack.append(oper.pop())
                oper.append(ch)
            elif ch == "(":
                oper.append(ch)
            elif ch == ")":
                while oper:
                    ch_pop = oper.pop()
                    if ch_pop == "(":
                        break
                    stack.append(ch_pop)
    return stack

def calc(stack):
    numstack = []
    for item in stack:
        if item in operations:
            b, a = numstack.pop(), numstack.pop()
            numstack.append(function[item](a, b))
        else:
            numstack.append(item)

    return numstack[0]

file = open("input.txt", "r")
s = file.readline()

time_beg = time.time()
st = rpn(s)
print("\n***Total time =  %.6f***" % (time.time() - time_beg))
time_beg = time.time()

for i in range(1000000):
    res = calc(st)

print("string = %s" % s)
print("stack = %s" % st)
print("res = %.6f" % res)
print("\n***Total time =  %.6f***" % (time.time() - time_beg))
