class Solution(object):
    def evalRPN(self, tokens):
        res = 0
        stack = []
        for t in tokens:
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            else:
                tmp2 = stack.pop()
                tmp1 = stack.pop()
                if t == "+":
                    res = self.add(tmp1, tmp2)
                elif t == "-":
                    res = self.minus(tmp1, tmp2)
                elif t == "*":
                    res = self.multiply(tmp1, tmp2)
                elif t == "/":
                    res = self.divide(tmp1, tmp2)
                stack.append(res)

        return stack[0]

    def add(self, x, y):
        return x + y
    def minus(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        return x / y

test = Solution()
print test.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])