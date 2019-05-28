class Solution(object):
    def removeInvalidParentheses(self, s):
        res = []
        queue = [s]
        visited = set([s])
        found = False
        while queue:
            cur = queue.pop(0)
            if self.isValid(cur):
                found = True
                res.append(cur)
            elif not found:
                # for each str in queue, attempt to rm parentheses from head to toe
                for i in xrange(len(cur)):
                    # Remove '(' or ')'
                    if cur[i] == '(' or cur[i] == ')':
                        tmp = cur[:i] + cur[i + 1:]
                        if tmp not in visited:
                            # add removed 1 parentheses str into queue
                            queue.append(tmp)
                            visited.add(tmp)

        return res

    def isValid(self, s):
        stack = []
        dict = {")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False

        if stack == []:
            return True

test = Solution()
print test.removeInvalidParentheses("(A)(()")

# Tip: define global var
# def f1():
#     global res
#     res = []
# def f2():
#     res.append(something)