class Solution:
    # @param {string} s a string
    # @param {string} p a non-empty string
    # @return {int[]} a list of index
    def findAnagrams(self, s, p):

        res = []

        # get p into dict
        dic_p = {}
        for j in p:
            dic_p[j] = dic_p.get(j, 0) + 1
        # implement strStr
        for i in range(len(s) - len(p) + 1):
            # get s into dict
            dic_s = {}
            for num in s[i:i + len(p)]:
                dic_s[num] = dic_s.get(num, 0) + 1
            # compare dic_s and dic_p
            if dic_s == dic_p:
                res.append(i)

        return res

    def findAnagrams2(self, s, p):
        if len(s) < len(p):
            return []

        res = []
        dic_p = {}
        dic_s = {}

        for j in p:
            dic_p[j] = dic_p.get(j, 0) + 1

        for i in range(len(p)):
            dic_s[s[i]] = dic_s.get(s[i], 0) + 1

        if dic_p == dic_s:
            res.append(0)

        for k in range(len(p), len(s)):
            front = s[k - len(p)]
            end = s[k]
            # Remove front key
            dic_s[front] -= 1
            if dic_s[front] == 0:
                dic_s.pop(front)

            # Push end
            dic_s[end] = dic_s.get(end, 0) + 1

            # If found, i.e. k = 8, len(p) = 3, append(6)
            if dic_p == dic_s:
                res.append(k - len(p) + 1)

        return res

test = Solution()
print test.findAnagrams2("cbaebabacd", "abc")