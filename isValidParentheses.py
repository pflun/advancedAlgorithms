class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            # If accept other characters "ABCDEF"
            else:
                return False
        return stack == []

    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        dic = {'}': '{', ')': '(', ']': '['}
        stack = []
        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if curr != dic[c]:
                    return False
        return True if len(stack) == 0 else False

test = Solution()
print test.isValidParentheses("(A)[]{}")
print test.isValidParentheses("()[]{}")