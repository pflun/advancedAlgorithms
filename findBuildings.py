class Solution(object):
    def findBuildings(self, heights):
        to_right_max_heights = heights[-1]
        res = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] <= to_right_max_heights:
                continue
            else:
                to_right_max_heights = heights[i]
                # prepend i at index 0, don't use [i] + res it will TLE
                res.insert(0, i)
        return res
