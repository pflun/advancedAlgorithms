class Solution(object):
    def checkIfPangram(self, sentence):
        visited = set()
        for c in sentence:
            visited.add(c)
        return True if len(visited) == 26 else False

test = Solution()
print test.checkIfPangram('thequickbrownfoxjumpsoverthelazydog')