import heapq
import string
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paraList = paragraph.split(" ")
        dic = {}
        for p in paraList:
            # remove punctuation
            if p[-1] in string.punctuation:
                p = p[:-1]
            dic[p] = dic.get(p, 0) + 1

        heap = []
        heapq.heapify(heap)

        for key, val in dic.items():
            heapq.heappush(heap, [self.negativify(val), key])

        while heap:
            freq, word = heapq.heappop(heap)
            if word.lower() not in banned:
                return word.lower()

        return ""

    def negativify(self, n):
        n = -n
        return n

test = Solution()
print test.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])