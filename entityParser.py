class Solution(object):
    def entityParser(self, text):
        dic = {'&quot;':'"', '&apos;':"'", "&amp;":'&', '&gt;':'>', '&lt;':'<', '&frasl;':'/'}
        res = ''
        i = 0
        while i < len(text):
            if text[i] != '&':
                res += text[i]
            else:
                if i + 7 <= len(text) and text[i:i + 7] in dic:
                    res += dic[text[i:i + 7]]
                    i += 7
                    continue
                elif i + 6 <= len(text) and text[i:i + 6] in dic:
                    res += dic[text[i:i + 6]]
                    i += 6
                    continue
                elif i + 5 <= len(text) and text[i:i + 5] in dic:
                    res += dic[text[i:i + 5]]
                    i += 5
                    continue
                elif i + 4 <= len(text) and text[i:i + 4] in dic:
                    res += dic[text[i:i + 4]]
                    i += 4
                    continue
                else:
                    res += text[i]
            i += 1
        return res

test = Solution()
print test.entityParser("&amp; is an HTML entity but &ambassador; is not.")
print test.entityParser("and I quote: &quot;...&quot;")
print test.entityParser("Stay home! Practice on Leetcode :)")
print test.entityParser("x &gt; y &amp;&amp; x &lt; y is always false")
print test.entityParser("leetcode.com&frasl;problemset&frasl;all")