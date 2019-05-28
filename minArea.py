class Solution:
    def minArea(self, image, x, y):
        self.top = len(image)
        self.bottom = 0
        self.left = len(image[0])
        self.right = 0

        def dfs(image, x, y):
            if x < 0 or x >= len(image) or y < 0 or y > len(image[0]) or image[x][y] != "1":
                return
            self.top = min(self.top, x)
            self.bottom = max(self.bottom, x)
            self.left = min(self.left, y)
            self.right = max(self.right, y)
            # Mark "2" as visited
            image[x] = image[x][:y - 1] + "2" + image[x][y:]
            dfs(image, x + 1, y)
            dfs(image, x - 1, y)
            dfs(image, x, y + 1)
            dfs(image, x, y - 1)

        dfs(image, x, y)
        print self.right, self.left, self.bottom, self.top
        return (self.right - self.left) * (self.bottom - self.top)

test = Solution()
print test.minArea([
  "0010",
  "0110",
  "0100"
], 0, 2)