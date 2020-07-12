class Solution(object):
    def getFolderNames(self, names):
        used = set()
        dic = {}
        res = []
        i = 0
        while i < len(names):
            cnt = 0
            curr = names[i]
            if curr not in dic:
                used.add(curr)
                dic[curr] = 0
                res.append(curr)
            else:
                currCnt = dic[curr]
                cnt = currCnt + 1
                newCurr = curr + '(' + str(cnt) + ')'
                while newCurr in used:
                    cnt += 1
                    newCurr = curr + '(' + str(cnt) + ')'
                    dic[curr] += 1
                else:
                    used.add(newCurr)
                    dic[newCurr] = 0
                    res.append(newCurr)
            i += 1
        return res

test = Solution()
print test.getFolderNames(["pes","fifa","gta","pes(2019)"])
print test.getFolderNames(["gta","gta(1)","gta","avalon"])
print test.getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"])
print test.getFolderNames(["wano","wano","wano","wano"])
print test.getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"])
print test.getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"])