class Add:

    def __init__(self,val1 ,val2):
        self.val1 = val1
        self.val2 = val2
    def add(self):
        return self.val1 + self.val2


class Subtract:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def subtract(self):
        return self.val1 - self.val2

class Mult:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def mult(self):
        return self.val1*self.val2

class Div:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def div(self):
        return self.val1/self.val2


def isOp(c):
    if c != "":
        return (c in "+-*/")
    else:
        return False


def pri(c):  # operator priority
    if c in "+-": return 0
    if c in "*/": return 1


def isNum(c):
    if c != "":
        return (c in "0123456789.")
    else:
        return False


def calc(op, num1, num2):
    if op == "+":
        a = Add(float(num1),float(num2))
        return str(a.add())
    if op == "-":
        s = Subtract(float(num1), float(num2))
        return str(s.subtract())
    if op == "*":
        m = Mult(float(num1), float(num2))
        return str(m.mult())
    if op == "/":
        d = Div(float(num1), float(num2))
        return str(d.div())


def Infix(expr):
    expr = list(expr)
    stackChr = list()  # character stack
    stackNum = list()  # number stack
    num = ""
    while len(expr) > 0:
        c = expr.pop(0)
        if len(expr) > 0:
            d = expr[0]
        else:
            d = ""
        if isNum(c):
            num += c
            if not isNum(d):
                stackNum.append(num)
                num = ""
        elif isOp(c):
            while True:
                if len(stackChr) > 0:
                    top = stackChr[-1]
                else:
                    top = ""
                if isOp(top):
                    if not pri(c) > pri(top):
                        num2 = stackNum.pop()
                        op = stackChr.pop()
                        num1 = stackNum.pop()
                        stackNum.append(calc(op, num1, num2))
                    else:
                        stackChr.append(c)
                        break
                else:
                    stackChr.append(c)
                    break
        elif c == "(":
            stackChr.append(c)
        elif c == ")":
            while len(stackChr) > 0:
                c = stackChr.pop()
                if c == "(":
                    break
                elif isOp(c):
                    num2 = stackNum.pop()
                    num1 = stackNum.pop()
                    stackNum.append(calc(c, num1, num2))

    while len(stackChr) > 0:
        c = stackChr.pop()
        if c == "(":
            break
        elif isOp(c):
            num2 = stackNum.pop()
            num1 = stackNum.pop()
            stackNum.append(calc(c, num1, num2))

    return stackNum.pop()


# TEST
# expr = input("Enter the Expression")
# print("EXPR: " + expr)
# print("EVAL: " + str(eval(expr)))
# print("INFX: " + Infix(expr))
