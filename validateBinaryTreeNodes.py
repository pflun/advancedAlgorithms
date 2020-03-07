class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        indegree = [0 for _ in range(n)]
        for i in range(len(leftChild)):
            if leftChild[i] == -1:
                continue
            indegree[leftChild[i]] += 1
        for j in range(len(rightChild)):
            if rightChild[j] == -1:
                continue
            indegree[rightChild[j]] += 1
        if indegree[0] != 0:
            return False
        for i in range(1, n):
            if indegree[i] != 1:
                return False
        return True

test = Solution()
print test.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1])
print test.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1])
print test.validateBinaryTreeNodes(2, [1,0], [-1,-1])
print test.validateBinaryTreeNodes(6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1])