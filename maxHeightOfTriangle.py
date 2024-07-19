class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        if red == blue == 1:
            return 1
        res = 1
        red_copy = red
        blue_copy = blue
        i = 1
        next = True
        # try red first
        while red_copy >= 0 and blue_copy >= 0:
            if next:
                red_copy -= i
            else:
                blue_copy -= i
            if red_copy >= 0 and blue_copy >= 0:
                res = max(res, i)
            i += 1
            next = not next

        # try blue first
        red_copy = red
        blue_copy = blue
        i = 1
        next = False
        while red_copy >= 0 and blue_copy >= 0:
            if next:
                red_copy -= i
            else:
                blue_copy -= i
            if red_copy >= 0 and blue_copy >= 0:
                res = max(res, i)
            i += 1
            next = not next
        return res

test = Solution()
print test.maxHeightOfTriangle(2, 4)
print test.maxHeightOfTriangle(2, 1)
print test.maxHeightOfTriangle(1, 1)
print test.maxHeightOfTriangle(10, 1)
print test.maxHeightOfTriangle(1, 10)
print test.maxHeightOfTriangle(10, 10)