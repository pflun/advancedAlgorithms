class Solution(object):
    def queryResults(self, limit, queries):
        res = []
        colorsToBalls = {}
        ballToColors = {}
        for q in queries:
            ball = q[0]
            color = q[1]
            if ball not in ballToColors:
                ballToColors[ball] = color
                if color not in colorsToBalls:
                    colorsToBalls[color] = set([ball])
                else:
                    colorsToBalls[color].add(ball)
            else:
                oldColor = ballToColors[ball]
                ballToColors[ball] = color
                # remove old color from colorsToBalls
                if len(colorsToBalls[oldColor]) == 1:
                    del colorsToBalls[oldColor]
                else:
                    colorsToBalls[oldColor].remove(ball)
                # add new color to colorsToBalls
                if color not in colorsToBalls:
                    colorsToBalls[color] = set([ball])
                else:
                    colorsToBalls[color].add(ball)
            res.append(len(colorsToBalls))
        return res

test = Solution()
print test.queryResults(4, [[1,4],[2,5],[1,3],[3,4]])
print test.queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]])
print test.queryResults(1, [[0,1],[0,4],[0,4],[0,1],[1,2]])