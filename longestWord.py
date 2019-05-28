# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=TqrZg4wYP1U
# brutal force, this can also be solved by Trie
class Solution(object):
    def longestWord(self, words):
        res = ''
        s = set(words)

        for word in words:
            # 剪枝：如果当前长度已经小于res长度 or 同样长但lexicographical更大
            if len(word) < len(res) or len(word) == len(res) and word > res:
                continue
            prefix = ''
            valid = True
            # 把单词每个字符加到prefix上，查找prefix是否在set里，不在就利用valid退出循环
            for char in word:
                if valid is True:
                    prefix += char
                    if prefix not in s:
                        valid = False
            if valid is True:
                res = word

        return res

test = Solution()
print test.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])