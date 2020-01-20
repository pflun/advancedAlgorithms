class Solution(object):
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        for _ in range(len(nums) / k):
            curr = min(dic.keys())
            dic[curr] -= 1
            if dic[curr] == 0:
                del dic[curr]
            for i in range(k - 1):
                next = curr + i + 1
                if next not in dic:
                    return False
                else:
                    dic[next] -= 1
                    if dic[next] == 0:
                        del dic[next]
        return True

test = Solution()
print test.isPossibleDivide([1,2,3,3,4,4,5,6], 4)
print test.isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 3)
print test.isPossibleDivide([3,3,2,2,1,1], 3)
print test.isPossibleDivide([1,2,3,4], 3)