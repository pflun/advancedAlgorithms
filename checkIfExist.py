class Solution(object):
    def checkIfExist(self, arr):
        zeros = 0
        for a in arr:
            if a == 0:
                zeros += 1
            if zeros > 1:
                return True
        hashSet = set(arr)
        for a in arr:
            if a != 0 and a * 2 in hashSet:
                return True
        return False

test = Solution()
print test.checkIfExist([10,2,5,3])
print test.checkIfExist([7,1,14,11])
print test.checkIfExist([3,1,7,11])
print test.checkIfExist([-2,0,10,-19,4,6,-8])
print test.checkIfExist([0, 0])