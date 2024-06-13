class Solution(object):
    def rotateTheBox(self, box):
        for j in range(len(box)):
            for i in range(len(box[0]) - 1, -1, -1):
                if box[j][i] == "." or box[j][i] == "*":
                    continue
                box[j][i] = "."
                for k in range(i, len(box[0])):
                    if k == len(box[0]) - 1 or box[j][k + 1] == "#" or box[j][k + 1] == "*":
                        box[j][k] = "#"
                        break
        res = [[None for _ in range(len(box))] for _ in range(len(box[0]))]
        for j in range(len(box)):
            for i in range(len(box[0])):
                res[i][len(box) - j - 1] = box[j][i]
        return res

test = Solution()
print test.rotateTheBox([["#",".","*","."],
                        ["#","#","*","."]])
print test.rotateTheBox([["#","#","*",".","*","."],
                        ["#","#","#","*",".","."],
                        ["#","#","#",".","#","."]])