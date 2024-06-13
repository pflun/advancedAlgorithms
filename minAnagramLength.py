class Solution(object):
    def minAnagramLength(self, s):
        if len(s) == 1:
            return 1
        # if i > half of s, there's no need to continue
        # Try from length 1 to 50% of s and see if they can form valid anagrams
        for i in range(1, (len(s) / 2) + 1):
            if len(s) % i == 0 and self.valid(s, i):
                return i
        return len(s)

    # divide s into k group and validate if they're all anagrams
    def valid(self, s, k):
        anagrams = []
        i = 0
        while i < len(s):
            anagrams.append(s[i:i + k])
            i += k
        sortedTarget = sorted(anagrams[0])
        for j in range(1, len(anagrams)):
            # found not anagram
            if sorted(anagrams[j]) != sortedTarget:
                return False
        return True

test = Solution()
print test.minAnagramLength("abba")
print test.minAnagramLength("cdef")
print test.minAnagramLength("aabb")
