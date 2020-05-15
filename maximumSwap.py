class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = list(str(num))
        maxV = sorted(res, reverse=True)

        if int(res[0]) != int(maxV[0]):
            res = self.swap(0, maxV[0], res)

        # if can swap at most twice
        # if int(res[1]) != int(maxV[1]):
        #     res = self.swap(1, maxV[1], res)

        return int(''.join(res))

    def swap(self, start, target, res):
        for i in range(len(res)):
            if res[i] == target:
                res[start], res[i] = res[i], res[start]
        return res

test = Solution()
print test.maximumSwap(2736)
print test.maximumSwap(9973)