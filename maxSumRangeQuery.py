class Solution(object):
    # use trick to pass OJ, basically Prefix Sum
    # for each request = [start, end], we let t[start] += 1, indicate that every index after this point will be counted 1 more time because of this request,
    # and t[end + 1] -= 1, indicate that every index after end will be counted 1 less time because of the end of this request.
    # Now the prefix sum of this array t is corresponds to the number of requests for each index. We choose array t has length len(nums) + 1,
    # only because we need to ensure end + 1 is within the range when we put t[end+1] -= 1. To compute the number of requests for indices, we will only count the first len(nums) prefix sums.
    def maxSumRangeQuery2(self, nums, requests):
        mod = 10 ** 9 + 7
        n = len(nums)
        t = [0] * (n + 1)
        for a, b in requests:
            t[a] += 1
            t[b + 1] -= 1
        for i in range(1, n):
            t[i] += t[i - 1]

        nums.sort()
        t.pop()
        t.sort()

        return sum(a * b for a, b in zip(nums, t)) % mod

    # TLE
    def maxSumRangeQuery(self, nums, requests):
        res = 0
        dic = {}
        for r in requests:
            for i in range(r[0], r[1] + 1):
                dic[i] = dic.get(i, 0) + 1
        nums.sort()
        for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True):
            n = nums.pop()
            res += v * n
        return res % (10 ** 9 + 7)

test = Solution()
print test.maxSumRangeQuery([1,2,3,4,5], [[1,3],[0,1]])
print test.maxSumRangeQuery([1,2,3,4,5,6], [[0,1]])
print test.maxSumRangeQuery([1,2,3,4,5,10], [[0,2],[1,3],[1,1]])