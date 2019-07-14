# https://www.youtube.com/watch?v=u_Wc4jwrp3Q&t=874s
# permutation + preprocess + pruning
class Solution(object):
    def shortestSuperstring(self, A):
        self.res = []
        self.cost = []
        for i in range(len(A)):
            tmp = []
            for j in range(len(A)):
                if i == j:
                    tmp.append(0)
                tmp.append(self.getCost(A[i], A[j]))
            self.cost.append(tmp)

        def dfs(A, used, tmp):
            if len(tmp) == len(A):
                self.res.append(tmp[:])

            for i in range(len(A)):
                if A[i] in used:
                    continue
                tmp.append(A[i])
                used.add(A[i])
                dfs(A, used, tmp)
                tmp.pop()
                used.remove(A[i])

        dfs(A, set(), [])
        return self.res

    # put w2 after w1, return length after merge?
    def getCost(self, w1, w2):
        if len(w1) > len(w2):
            for i in range(len(w1) - len(w2) + 1):
                if w1[i:len(w2)] == w2:
                    return len(w1)
        # continue

test = Solution()
print test.shortestSuperstring(["alex","loves","leetcode"])