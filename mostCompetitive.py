class Solution(object):
    def mostCompetitive(self, A, k):
        stack = []
        for i, a in enumerate(A):
            while stack and stack[-1] > a and len(stack) - 1 + len(A) - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(a)
        return stack

test = Solution()
print test.mostCompetitive([3,5,2,6], 2)
print test.mostCompetitive([2,4,3,3,5,4,9,6], 4)