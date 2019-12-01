# Given a string s consisting of n lowercase letters, you have to delete
# the minimum number of characters from s so that every letter in s appears a unique number of times.
# We only care about the occurrences of letters that appear at least once in result.
# Input: "aabbffddeaee"
# Output: 6
# Explanation:
# For example, we can delete all occurences of 'e' and 'f' and one occurence of 'd' to obtain the word "aabbda".
# Note that both 'e' and 'f' will occur zero times in the new word, but that's fine, since we only care about the letter that appear at least once.
class Solution(object):
    def minDeletionFreqUnique(self, string):
        dic = {}
        freq = {}
        for c in string:
            dic[c] = dic.get(c, 0) + 1
        for k, v in dic.items():
            freq[v] = freq.get(v, []) + [k]
        cnt = 0
        for k, v in freq.items():
            if len(v) > 1:
                for i in range(1, len(v)):
                    v = v[:i] + v[i + 1:]
                    nextIdx = k
                    while nextIdx in freq:
                        nextIdx -= 1
                    if nextIdx == 0:
                        cnt += k
                    else:
                        freq[nextIdx] = [v[i]]
                        cnt += k - nextIdx
        return cnt

test = Solution()
print test.minDeletionFreqUnique("aabbffddeaee")