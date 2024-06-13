# "AAA" => ""
# "BAAA" => "B" stack: [[B, 1]]
# "BAAABB" => "" stack: [[B, 1]] => [[B, 3]]
class Solution(object):
    def candyCrush(self, candy):
        # [curr, cnt]
        stack = [[candy[0], 1]]
        for i in range(1, len(candy)):
            if candy[i] == stack[-1][0]:
                stack[-1][1] += 1
            else:
                if stack[-1][1] >= 3:
                    stack.pop()
                if stack and stack[-1][0] == candy[i]:
                    stack[-1][1] += 1
                else:
                    stack.append([candy[i], 1])
        if stack[-1][1] >= 3:
            stack.pop()
        res = ""
        for s in stack:
            res += s[1] * s[0]
        return res

test = Solution()
print test.candyCrush("BAAA")
print test.candyCrush("BAAABB")