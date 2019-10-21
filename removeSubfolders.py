class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        res = []
        hashSet = set(folder)
        for d in folder:
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
print test.removeSubfolders(['/ab/cd/efg', '/ab/cd', '/df', '/gh'])
print test.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])
print test.removeSubfolders(["/a","/a/b/c","/a/b/d"])
print test.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])