# https://www.youtube.com/watch?v=8oOhXcdXbZk
# Output must be [ -, -, -, ..., +, +, + ]
class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for i in range(len(asteroids)):
            curr = asteroids[i]
            if curr > 0:
                stack.append(curr)
            else:
                # stack empty or all elements in stack are negative
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(curr)
                # stack top is positive
                elif abs(stack[-1]) == abs(curr):
                    # destroy stack top, do NOT append curr
                    stack.pop()
                elif abs(stack[-1]) < abs(curr):
                    stack.pop()
                    # curr alive, curr remain the same in next for loop
                    i -= 1
                # elif abs(stack[-1]) > abs(curr): Do Nothing, curr will be destroy automatically by not append

        return stack

test = Solution()
print test.asteroidCollision([10, 2, -5])