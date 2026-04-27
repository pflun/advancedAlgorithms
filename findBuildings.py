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

    def findBuildings2(self, heights):
        maxHeight = heights[-1]
        # rightmost building has no obstructed view
        res = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > maxHeight:
                res.append(i)
                maxHeight = heights[i]
        return res[::-1]

test = Solution()
print test.findBuildings2([4, 2, 3, 1])
print test.findBuildings2([4, 3, 2, 1])
print test.findBuildings2([1, 3, 2, 4])

# Follow-up: Ocean View from Both Sides
