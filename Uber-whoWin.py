# You will be given array of size N with integers numbered 1 to N in random order and a number k.
# for eg. arr = 2 1 3 4 5, k = 2
#
# Let these players are standing in a queue in a given order, first two players will play a game then whose value is greater will win and the lost one will go to end of a queue.
# Whoever player will win consecutive k games is the winner of game.
#
# In the above example,
# first match b/w : 2 & 1
# second match b/w : 2 & 3
# third match b/w : 3 & 4
# fourth match b/w : 4 & 5
# fifth match b/w : 5 & 1
#
# 5 won 2 matches consecutively: 5 is winner
#
# Solution should be O(n) in time and 0(1) in space. arr is immutable
class Solution(object):
    def whoWin(self, arr, k):
        if len(arr) < 2:
            return
        cnt = 0
        prev = arr[0]
        # cnt == k means consecutive wont k times
        while cnt < k:
            prevIdx = 0
            if prev == arr[0]:
                curr = arr[1]
                prevIdx = 0
            elif prev == arr[1]:
                curr = arr[0]
                prevIdx = 1
            if prev > curr:
                cnt += 1
                # move curr from second slot to end of queue
                if prevIdx == 0:
                    arr = [arr[0]] + arr[2:] + [arr[1]]
                else:
                    arr = arr[1:] + [arr[0]]
            else:
                cnt = 1
                prev = curr
                if prevIdx == 0:
                    arr = arr[1:] + [arr[0]]
                else:
                    # move prev from second slot to end of queue
                    arr = [arr[0]] + arr[2:] + [arr[1]]
        return prev

test = Solution()
print test.whoWin([2,1,3,4,5], 2)