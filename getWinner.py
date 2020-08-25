class Solution(object):
    def getWinner(self, arr, k):
        if k >= len(arr):
            return max(arr)
        winner = None
        cnt = 0
        while cnt < k:
            first = arr.pop(0)
            second = arr.pop(0)
            if first > second:
                tmpWinner = first
                # arr = [first] + arr + [second]
                arr.insert(0, first)
                arr.append(second)
                if not winner:
                    winner = tmpWinner
                    cnt = 1
                else:
                    if winner == tmpWinner:
                        cnt += 1
                    else:
                        winner = tmpWinner
                        cnt = 1
            else:
                tmpWinner = second
                # arr = [second] + arr + [first]
                arr.insert(0, second)
                arr.append(first)
                if not winner:
                    winner = tmpWinner
                    cnt = 1
                else:
                    if winner == tmpWinner:
                        cnt += 1
                    else:
                        winner = tmpWinner
                        cnt = 1
            if cnt == k:
                return winner

test = Solution()
print test.getWinner([2,1,3,5,4,6,7], 2)
print test.getWinner([3,2,1], 10)
print test.getWinner([1,9,8,2,3,7,6,4,5], 7)
print test.getWinner([1,11,22,33,44,55,66,77,88,99], 1000000000)
print test.getWinner([1,25,35,42,68,70], 1)