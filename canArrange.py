class Solution(object):
    def canArrange(self, arr, k):
        if len(arr) % 2 != 0:
            return False
        dic = {}
        for i in range(len(arr)):
            reminder = arr[i] % k
            dic[reminder] = dic.get(reminder, 0) + 1
        for i in range(len(arr)):
            reminder = arr[i] % k
            if reminder == 0:
                if dic[reminder] % 2 == 1:
                    return False
            elif reminder * 2 == k:
                if dic[reminder] % 2 == 1:
                    return False
            else:
                if k - reminder in dic and reminder in dic and dic[k - reminder] != dic[reminder]:
                    return False
        return True

test = Solution()
# print test.canArrange([1,2,3,4,5,10,6,7,8,9], 5)
# print test.canArrange([1,2,3,4,5,6], 7)
# print test.canArrange([1,2,3,4,5,6], 10)
# print test.canArrange([-10,10], 2)
# print test.canArrange([-1,1,-2,2,-3,3,-4,4], 3)
print test.canArrange([6521,-2703,1854,-6116,7093,-9610,1458,1025,9093,8347,3126,-6106,8104,2824], 76)
print test.canArrange([-1,1,-2,2,-3,3,-4,4], 3)