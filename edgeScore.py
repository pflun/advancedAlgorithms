class Solution(object):
    def edgeScore(self, edges):
        candidates = [0 for _ in range(len(edges))]
        for i in range(len(edges)):
            candidates[edges[i]] += i
        maxIdx = 0
        maxVal = 0
        for i in range(len(candidates)):
            if candidates[i] > maxVal:
                maxIdx = i
                maxVal = candidates[i]
        return maxIdx