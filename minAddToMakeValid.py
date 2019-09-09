class Solution(object):
    def minAddToMakeValid(self, S):
        step = 0
        queue = [S]

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if self.isValid(curr):
                    return step
                for i in range(len(curr) + 1):
                    queue.append(curr[:i] + '(' + curr[i:])
                    queue.append(curr[:i] + ')' + curr[i:])

            step += 1

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
print test.minAddToMakeValid("(((")
