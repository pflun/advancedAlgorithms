import heapq
class Solution(object):
    def func(self, string):
        # tmp = list(string)
        # tmp = set(tmp)
        # return ''.join(tmp)
        # newstr = string.replace("A", "")
        string = list(string)
        for char in string:
            if char == 'A':
                string.remove('A')
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, [2, 'bbb'])
        heapq.heappush(heap, [3, 'ccc'])
        heapq.heappush(heap, [1, 'aaa'])
        while heap:
            print heapq.heappop(heap)
        return string

    def findMinCoins(self, coins, target):
        self.res = float('inf')

        def dfs(coins, target, i,  sum, number):
            if sum > target or i == len(coins):
                return
            elif sum == target:
                self.res = min(self.res, number)
            else:
                dfs(coins, target, i, sum + coins[i], number + 1)
                if i < len(coins) - 1:
                    dfs(coins, target, i + 1, sum + coins[i + 1], number + 1)

        for i in range(len(coins)):
            dfs(coins, target, i, coins[i], 1)

        return self.res


test1 = Solution()
print test1.func("ADOBECODEBANC")
print type(bin(4))

print test1.findMinCoins([1, 2, 5, 10], 27)
print max([1, 2, 5, 10])

def anythree(nums):

    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                tmp = nums[i] + nums[j] + nums[k]
                res.append(tmp)

    return res

print anythree([1, 2, 5, 10])

def dupli(nums):
    nums = set(nums)
    res = []
    for num in nums:
        res.append(num)

    return res
print dupli([1, 2, 5, 5])

dp = [[1 for _ in range(5)] for _ in range(5)]
dp[3][3] = 2
print dp

class Solution(object):
    def findBottomLeftValue(self, root):
        if root is None:
            return None
        self.dic = {}
        maxkey = 0

        def dfs(root, depth):
            self.dic[depth] = root.val
            if root.right:
                dfs(root.right, depth + 1)
            if root.left:
                dfs(root.left, depth + 1)

        dfs(root, 0)

        for key, val in self.dic.items():
            if key >= maxkey:
                res = val

        return res

def maxArray(nums):
    if not nums:
        return nums
    max_val = nums[0]
    cur_sum = 0
    temp = []
    res = [nums[0]]
    nums_len = len(nums)
    for i in range(nums_len):
        if cur_sum < 0:
            cur_sum = 0
            temp = []
        cur_sum += nums[i]
        temp.append(nums[i])
        # print cur_sum, max_val, temp, res
        if cur_sum > max_val:
            max_val = cur_sum
            res = temp[:nums_len]
    # print "start", start
    # print end#nums[start:end + 1]
    return res, max_val


nums = [-2, 1, -3, 4, -1, 2, 1, -5, -4]

print maxArray(nums)
space = " "
num1 = 10
while num1 > 0:
    if num1 % 2 == 0:
        space = space + "0"
    else:
        space = space + "1"
    num1 = int(num1 / 2)
else:
    space = space[::-1]
    print(space)
