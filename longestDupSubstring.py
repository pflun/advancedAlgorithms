# https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/Python-Binary-search-O(n-log-n)-average-with-Rabin-Karp-explained
class Solution:
    # rolling-hash, dic: hash => [start_index]
    def RabinKarp(self, text, M, q):
        if M == 0: return True
        h, t, d = (1 << (8 * M - 8)) % q, 0, 256

        dic = defaultdict(list)

        for i in range(M):
            t = (d * t + ord(text[i])) % q

        dic[t].append(i - M + 1)

        for i in range(len(text) - M):
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            for j in dic[t]:
                if text[i + 1:i + M + 1] == text[j:j + M]:
                    return (True, text[j:j + M])
            dic[t].append(i + 1)
        return (False, "")

    # binary search find duplicate substring at length mid, if mid can find meaning mid - 1, -2 ... can find, so try longer substring (began = mid)
    def longestDupSubstring(self, S):
        beg, end = 0, len(S)
        q = (1 << 31) - 1
        Found = ""
        while beg + 1 < end:
            mid = (beg + end) // 2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found
