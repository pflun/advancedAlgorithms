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

test = Solution()
print test.isValidParentheses("(A)[]{}")