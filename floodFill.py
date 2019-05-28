class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        if len(image) == 0 or sr > len(image) - 1 or sc > len(image[0]) - 1:
            return []
        elif not newColor or image[sr][sc] == newColor:
            return image

        def fill(image, x, y, newColor, oldColor):
            if x < 0 or x > len(image) - 1 or y < 0 or y > len(image[0]) - 1 or image[x][y] != oldColor:
                return
            image[x][y] = newColor
            fill(image, x + 1, y, newColor, oldColor)
            fill(image, x - 1, y, newColor, oldColor)
            fill(image, x, y + 1, newColor, oldColor)
            fill(image, x, y - 1, newColor, oldColor)

        fill(image, sr, sc, newColor, image[sr][sc])

        return image

test = Solution()
print test.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print test.floodFill([[0,0,0],[0,1,1]], 1, 1, 1)