class Solution(object):
    def interpret(self, command):
        res = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
                i += 1
            elif i + 2 <= len(command) and command[i:i + 2] == '()':
                res += 'o'
                i += 2
            elif i + 4  <= len(command) and command[i:i + 4] == '(al)':
                res += 'al'
                i += 4
            else:
                break
        return res

test = Solution()
print test.interpret("G()(al)")
print test.interpret("G()()()()(al)")
print test.interpret("(al)G(al)()()G")
