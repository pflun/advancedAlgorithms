# https://leetcode.com/problems/best-team-with-no-conflicts/discuss/899475/Fairly-easy-DP
class Solution(object):
    def bestTeamScore(self, scores, ages):
        aToS = []
        for i in range(len(scores)):
            aToS.append([ages[i], scores[i]])
        aToS.sort(reverse=True)
        res = 0
        dp = [0 for _ in range(len(aToS) + 1)]
        for i in range(len(aToS)):
            score = aToS[i][1]
            dp[i] = score
            for j in range(i):
                if aToS[j][1] >= score:
                    dp[i] = max(dp[i], dp[j] + score)
            res = max(res, dp[i])

        return res

test= Solution()
print test.bestTeamScore([1,2,3,5], [8,9,10,1])