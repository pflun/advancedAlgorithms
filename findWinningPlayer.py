class Solution(object):
    def findWinningPlayer(self, skills, k):
        i = 0
        cnt = 0
        for j in range(1, len(skills)):
            if skills[i] < skills[j]:
                cnt = 0
                i = j
            cnt += 1
            if cnt == k:
                break
        return i

test = Solution()
print test.findWinningPlayer([4,2,6,3,9], 2)
print test.findWinningPlayer([2,5,4], 3)