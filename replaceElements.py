class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr = arr[::-1]
        res = [-1]
        for a in arr[:-1]:
            tmp = max(res[-1], a)
            res.append(tmp)
        return res[::-1]