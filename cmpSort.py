class Solution(object):
    def cmpSort(self, versions):
        def compare(x, y):
            if x > y:
                return 1
            elif x < y:
                return -1
            else:
                return 0

        return sorted(versions, cmp=lambda x, y: compare(x, y))

test = Solution()
print test.cmpSort(["0.0.2a", "0.2.1", "0.0.1", "0.0.2b"])