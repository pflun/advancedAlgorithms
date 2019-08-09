class Solution(object):
    def validWordSquare(self, words):
        if len(words) != len(words[0]):
            return False
        for j in range(len(words)):
            for i in range(len(words[0])):
                if words[j][i] != words[i][j]:
                    return False
        return True

test = Solution()
print test.validWordSquare([
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
])
print test.validWordSquare([
  "ball",
  "area",
  "read",
  "lady"
])