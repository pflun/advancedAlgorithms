# -*- coding: utf-8 -*-
class Solution(object):
    # 直接hash整个file
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

    # 先用size filter，再每次hash one line，直到全部file读完，num of files == num of isLastLine
    def findDuplicate2(self, paths):
        dic = {}
        # List<List<duplicated_path>>
        candidates = []
        # 第一步，先用size filter
        for p in paths:
            tmp = p.split(' ')
            tmpPath = tmp[0]
            size = self.getSize()
            dic[size] = dic.get(size, []) + [tmpPath]

        for v in dic.values():
            if len(v) > 1:
                candidates.append(v)

        # 第二步，每次hash一行
        # 退出条件是，全部file都读完，num of files == num of isLastLine
        while True:
            tmp = []
            numPath = 0
            cnt = 0
            # List<List<duplicated_path>>
            for c in candidates:
                dic = {}
                for p in c:
                    numPath += 1
                    # 对于当此循环每一个path numPath++，每读到一个isLastLine cnt++
                    if self.isLastLine(p):
                        cnt += 1
                    nextLine = self.readNextLine(p)
                    hashedVal = self.hash(nextLine, "MD5")
                    dic[hashedVal] = dic.get(hashedVal, []) + [p]
                # filter non duplicated path
                for k, v in dic.items():
                    if len(v) > 1:
                        tmp.append(v)
            candidates = tmp[:]
            # 档次循环total files == total isLastLine，退出
            if numPath == cnt:
                break
        return candidates


test = Solution()
print test.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])

# Followup 1, read entire file takes too much time
# Step 1, dic = { file.size() => [path1, path2]} and filter out non duplicated files
# Step 2, compute SHA256()
# Followup 2, Files with same size and same hash
# compare files byte by byte