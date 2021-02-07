class Solution:
    def calculate(self, s):
        def calc(idx):
            tot = partial = n = 0
            last = '+'

            while idx < len(s):
                i, el = idx, s[idx]
                if el.isdigit():
                    n = int(n) * 10 + int(el)
                elif el == '(':
                    idx, n = calc(idx + 1)
                elif el == ')':
                    break
                elif el in ops:
                    if el in ['+', '-']:
                        tot += ops[last](partial, n)
                        partial = 0
                    else:
                        partial = ops[last](partial, n)
                    last = el
                    n = 0
                idx += 1

            tot += ops[last](partial, n)
            return idx, tot

        ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: int(x / y)}

        return calc(0)[1]