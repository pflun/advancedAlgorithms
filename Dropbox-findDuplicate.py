class Solution(object):
    def findDuplicate(self, paths):
        # "efgh" => ["root/c/d/4.txt", "root/4.txt"]
        dic = {}
        res = []
        for p in paths:
            tmp = p.split(' ')
            tmpPath = tmp[0]
            for f in tmp[1:]:
                t = f.split('(')
                name = t[0]
                content = t[1][:-1]
                # SHA256(content) as key, or combination of file.size() + SHA256(content[:100])
                dic[content] = dic.get(content, []) + [tmpPath + '/' + name]

        for v in dic.values():
            if len(v) > 1:
                res.append(v)
        return res

test = Solution()
print test.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])

# Followup 1, read entire file takes too much time
# Step 1, dic = { file.size() => [path1, path2]} and filter out non duplicated files
# Step 2, compute SHA256()
# Followup 2, Files with same size and same hash
# compare files byte by byte