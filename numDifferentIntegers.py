class Solution(object):
    def numDifferentIntegers(self, word):
        hashSet = set()
        i = 0
        while i < len(word):
            if word[i].isdigit():
                num = int(word[i])
                while i + 1 < len(word) and word[i + 1].isdigit():
                    num = num * 10 + int(word[i + 1])
                    i += 1
                hashSet.add(num)
            i += 1
        return len(hashSet)

test = Solution()
print test.numDifferentIntegers("a123bc34d8ef34")
print test.numDifferentIntegers("leet1234code234")
print test.numDifferentIntegers("a1b01c001")