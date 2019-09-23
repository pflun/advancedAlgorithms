import heapq
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        self.res = []
        self.isOdd = True if k / 2 != 0 else False
        self.small = []
        self.large = []
        heapq.heapify(self.small)
        heapq.heapify(self.large)

        med = sorted(nums[:k])[k / 2]
        if self.isOdd:
            for n in nums[:k]:
                if n <= med:
                    heapq.heappush(self.small, -n)
                else:
                    heapq.heappush(self.large, n)
            self.res.append(-self.small[0])
        else:
            for n in nums[:k]:
                if n < med:
                    heapq.heappush(self.small, -n)
                else:
                    heapq.heappush(self.large, n)
            self.res.append((-self.small[0] + self.large[0]) / 2)
        # if duplicate exist, we need to re-balance

        for i in range(k, len(nums)):
            left = i - k
            if self.isOdd:
                # add right
                if nums[i] <= -self.small[0]:
                    heapq.heappush(self.small, -nums[i])
                else:
                    heapq.heappush(self.large, nums[i])
                # remove left
                if nums[left] <= -self.small[0]:
                    self.small.remove(-nums[left])
                    heapq.heapify(self.small)
                else:
                    self.large.remove(nums[left])
                    heapq.heapify(self.large)
                # re-balance
                if len(self.small) - len(self.large) == -1:
                    tmp = heapq.heappop(self.large)
                    heapq.heappush(self.small, -tmp)
                elif len(self.small) - len(self.large) == 3:
                    tmp = - heapq.heappop(self.small)
                    heapq.heappush(self.large, tmp)
                self.res.append(-self.small[0])
            else:
                # add right
                if nums[i] <= -self.small[0]:
                    heapq.heappush(self.small, -nums[i])
                else:
                    heapq.heappush(self.large, nums[i])
                # remove left
                if nums[left] <= -self.small[0]:
                    self.small.remove(-nums[left])
                    heapq.heapify(self.small)
                else:
                    self.large.remove(nums[left])
                    heapq.heapify(self.large)
                # re-balance
                if len(self.small) - len(self.large) == -2:
                    tmp = heapq.heappop(self.large)
                    heapq.heappush(self.small, -tmp)
                elif len(self.small) - len(self.large) == 2:
                    tmp = - heapq.heappop(self.small)
                    heapq.heappush(self.large, tmp)
                self.res.append((-self.small[0] + self.large[0]) / 2)
        return self.res

test = Solution()
print test.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
