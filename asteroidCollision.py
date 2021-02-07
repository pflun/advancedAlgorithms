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

    # Same: https://leetcode.com/problems/asteroid-collision/discuss/109666/Python-O(n)-Stack-based-with-explanation
    def asteroidCollision2(self, asteroids):
        res = []
        for asteroid in asteroids:
            # We only need to resolve collisions under the following conditions:
            # - stack is non-empty
            # - current asteroid is -ve
            # - top of the stack is +ve
            while len(res) and asteroid < 0 and res[-1] > 0:
                # Both asteroids are equal, destroy both.
                if res[-1] == -asteroid:
                    res.pop()
                    break
                # Stack top is smaller, remove the +ve asteroid
                # from the stack and continue the comparison.
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
                # Stack top is larger, -ve asteroid is destroyed.
                elif res[-1] > -asteroid:
                    break
            else:
                # -ve asteroid made it all the way to the
                # bottom of the stack and destroyed all asteroids.
                res.append(asteroid)
        return res

test = Solution()
print test.asteroidCollision([10, 2, -5])