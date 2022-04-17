# 702. Search in a Sorted Array of Unknown Size
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        low = 0
        high = 10000
        while low + 1 < high:
            mid = (low + high) / 2
            if reader.get(mid) == 2147483647 or reader.get(mid) > target:
                high = mid
            elif reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                low = mid
        if reader.get(low) == target:
            return low
        elif reader.get(high) == target:
            return high
        else:
            return -1

# Test won't work as first param is ArrayReader not Array
test = Solution()
print test.search([-1,0,3,5,9,12], 9)
print test.search([-1,0,3,5,9,12], 2)