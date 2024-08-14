class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        matrix = [[None for _ in range(n)] for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = cnt
                cnt += 1
        x = y = 0
        for c in commands:
            if c == 'UP':
                x -= 1
            elif c == 'DOWN':
                x += 1
            elif c == 'LEFT':
                y -= 1
            elif c == 'RIGHT':
                y += 1
        return matrix[x][y]

test = Solution()
print test.finalPositionOfSnake(2, ["RIGHT","DOWN"])
print test.finalPositionOfSnake(3, ["DOWN","RIGHT","UP"])