class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        rs = []
        s = filter(lambda name: name.strip(), s.split(' '))

        for i in range(len(s) - 1, -1, -1):
            rs.append(s[i])
        reversed_str = ' '.join(rs)
        return reversed_str

    # in-place
    def reverseWords2(self, s):
        # Three step to reverse
        # 1, reverse the whole sentence
        s = self.reverse(s, 0, len(s) - 1)

        # 2, reverse each word
        start = 0
        end = -1
        for i in range(len(s)):
            if s[i] == ' ':
                s = self.reverse(s, start, i - 1)
                start = i + 1
        # print s
        #  3, reverse the last word, if there is only one word this will solve the corner case
        s = self.reverse(s, start, len(s) - 1)
        return s


    def reverse(self, s, start, end):
        s = list(s)
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return "".join(s)

test = Solution()
print test.reverseWords2("the sky is blue")