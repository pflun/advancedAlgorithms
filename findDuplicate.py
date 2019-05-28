# 609. Find Duplicate File in System

class Solution(object):
    def findDuplicate(self, paths):
        import collections
        dic = collections.defaultdict(list)
        res = []

        for i in range(len(paths)):
            dir = paths[i].split(' ', 1)[0]
            tmp = paths[i].split(' ', 1)[1]
            nameContents = tmp.split(' ')

            for j in nameContents:
                idx1 = j.find("(")
                idx2 = j.find(")")
                name = j.split('(', 1)[0]
                content = j[idx1 + 1:idx2]
                dic[content].append(dir + '/' + name)

        for key, val in dic.items():
            if len(val) > 1:
                res.append(val)

        return res

test = Solution()
print test.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])