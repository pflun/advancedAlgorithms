# Note: [1,0,0,0] is a corner case where right[3] = 0 and left[3] = 3, res[3] = 0, need to fix
class Solution(object):
    def maxDistToClosest(self, seats):
        right = [0] * len(seats)
        res = [0] * len(seats)

        for i in range(len(seats)):
            if seats[i] == 0:
                for j in range(i, len(seats)):
                    if seats[j] == 1:
                        right[i] = j - i
                        break

        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 0:
                for j in range(i, -1, -1):
                    if seats[j] == 1:
                        leftDistance = i - j
                        res[i] = min(leftDistance, right[i])
                        break

        return max(res), right, res

test = Solution()
print test.maxDistToClosest([1,0,0,0])