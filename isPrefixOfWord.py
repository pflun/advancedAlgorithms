class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        arr = sentence.split(' ')
        for i in range(len(arr)):
            if len(arr[i]) >= len(searchWord) and arr[i][:len(searchWord)] == searchWord:
                return i + 1
        return -1

test = Solution()
print test.isPrefixOfWord("i love eating burger", "burg")
print test.isPrefixOfWord("this problem is an easy problem", "pro")
print test.isPrefixOfWord("i am tired", "you")
print test.isPrefixOfWord("i use triple pillow", "pill")
print test.isPrefixOfWord("hello from the other side", "they")