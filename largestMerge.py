class Solution(object):
    def largestMerge(self, word1, word2):
        merge = ''
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i == len(word1):
                merge += word2[j]
                j += 1
            elif j == len(word2):
                merge += word1[i]
                i += 1
            else:
                if word1[i] > word2[j]:
                    merge += word1[i]
                    i += 1
                elif word1[i] < word2[j]:
                    merge += word2[j]
                    j += 1
                else:
                    if word1[i:] > word2[j:]:
                        merge += word1[i]
                        i += 1
                    else:
                        merge += word2[j]
                        j += 1
        return merge

    # bug
    def largestMerge2(self, word1, word2):
        merge = ''
        p1 = 0
        p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            if word1[p1] > word2[p2]:
                merge += word1[p1]
                p1 += 1
            elif word1[p1] < word2[p2]:
                merge += word2[p2]
                p2 += 1
            else:
                isWordOne = self.findNext(word1, word2, p1, p2)
                if isWordOne == 0:
                    merge += word1[p1]
                    p1 += 1
                else:
                    merge += word2[p2]
                    p2 += 1
        if p1 <= len(word1) - 1:
            merge += word1[p1:]
        elif p2 < len(word2) - 1:
            merge += word2[p2:]
        return merge

    def findNext(self, word1, word2, p1, p2):
        while p1 < len(word1) and p2 < len(word2):
            if word1[p1] == word2[p2]:
                p1 += 1
                p2 += 1
            elif word1[p1] > word2[p2]:
                return 0
            else:
                return 1
        if p1 == len(word1):
            return 1
        else:
            return 2

test = Solution()
print test.largestMerge("cabaa", "bcaaa")
print test.largestMerge("abcabc", "abdcaba")
print test.largestMerge2("guguuuuuuuuuuuuuuguguuuuguug", "gguggggggguuggguugggggg")
# "nnnnpnnnnnennnnnnpnnennnnennnnennenpnnnnneenpnnee"
print test.largestMerge2("nnnnpnnennenpnnnnneenpnn", "nnnennnnnnpnnennnnennnnee")