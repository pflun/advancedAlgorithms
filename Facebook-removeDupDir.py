# -*- coding: utf-8 -*-
# 给你一个字符串数组，代表不同的路径，比如：
# [/ab/cd/efg, /ab/cd, /df, /gh]
# [/, /ab, /cd, /gh]
#
# 要求：
# 删掉那些冗余的子路径，比如 /ab/cd/efg 是 /ab/cd 的子路径（也就是说在这个目录下），所以就需要被删除。
# 注意: '/' 是根路径，是所有路径的父路径
class Solution(object):
    def removeDupDir(self, dirs):
        res = []
        hashSet = set(dirs)
        for d in dirs:
            # because ['', 'ab', 'cd'], 0 => '' and do Not include last folder
            dList = d.split('/')[1:-1]
            isExist = False
            prev = ''
            for f in dList:
                prev += '/' + f
                if prev in hashSet:
                    isExist = True
                    break
            if not isExist:
                res.append(d)
        return res

test = Solution()
print test.removeDupDir(['/ab/cd/efg', '/ab/cd', '/df', '/gh'])
print test.removeDupDir(["/a","/a/b","/c/d","/c/d/e","/c/f"])
print test.removeDupDir(["/a","/a/b/c","/a/b/d"])
print test.removeDupDir(["/a/b/c","/a/b/ca","/a/b/d"])