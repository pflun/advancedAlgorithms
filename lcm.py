# least common multiple
class Solution(object):
    def lcm(self, x, y):
        if x > y:
            greater = x
        else:
            greater = y

        while True:
            if greater % x == 0 and greater % y == 0:
                res = greater
                break
            greater += 1

        return res

test = Solution()
print test.lcm(2, 6)