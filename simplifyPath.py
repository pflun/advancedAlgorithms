class Solution(object):
    def simplifyPath(self, path):
        res = ''
        stack = []
        arr = path.split('/')
        for a in arr:
            if a == '.' or a == '':
                continue
            elif a == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(a)
        for s in stack:
            res += '/' + s
        if len(res) == 0:
            return '/'
        else:
            return res

test = Solution()
print test.simplifyPath("/a//b////c/d//././/..")