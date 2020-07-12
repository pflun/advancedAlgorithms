class Solution(object):
    def getStrongest(self, arr, k):
        if len(arr) == k:
            return arr
        arr.sort()
        if len(arr) % 2 != 0:
            med = arr[len(arr) / 2]
        else:
            med = arr[len(arr) / 2 - 1]
        i = 0
        j = len(arr) - 1
        res = []
        while len(res) < k and i < j:
            if abs(arr[i] - med) > abs(arr[j] - med):
                res.append(arr[i])
                i += 1
            elif abs(arr[i] - med) < abs(arr[j] - med):
                res.append(arr[j])
                j -= 1
            else:
                if arr[i] > arr[j]:
                    res.append(arr[i])
                    i += 1
                else:
                    res.append(arr[j])
                    j -= 1
        return res

test = Solution()
print test.getStrongest([1,2,3,4,5], 2)
print test.getStrongest([1,1,3,5,5], 2)
print test.getStrongest([6,7,11,7,6,8], 5)
print test.getStrongest([6,-3,7,2,11], 3)
print test.getStrongest([-7,22,17,3], 2)