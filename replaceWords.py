class Solution(object):
    def replaceWords(self, dict, sentence):
        rootSet = set(dict)
        list_sentence = sentence.split(' ')
        for j in range(len(list_sentence)):
            for i in range(len(list_sentence[j])):
                if list_sentence[j][:i] in rootSet:
                    list_sentence[j] = list_sentence[j][:i]
                    # No need to keep forloop if exist
                    break

        return " ".join(list_sentence)

test = Solution()
print test.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
