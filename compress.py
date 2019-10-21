class Solution(object):
    def compress(self, chars):
        idx = 0
        offset = 0
        while idx < len(chars):
            char, cnt = self.getNext(chars[idx:])
            chars[offset] = char
            chars[offset + 1] = str(cnt)
            offset += 2
            idx += cnt
        return len(chars[:offset])

    def getNext(self, arr):
        res = arr[0]
        cnt = 0
        i = 0
        while i < len(arr) and arr[i] == arr[0]:
            cnt += 1
            i += 1
        return res, cnt

test = Solution()
print test.compress(["a","a","a", "b","b","c","c","c"])