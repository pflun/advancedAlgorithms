class Solution(object):
    def rankTeams(self, votes):
        # {A: {0: 5}, B: {1: 2, 2: 3} ...}
        dic = {}
        for v in votes:
            for i in range(len(v)):
                if v[i] not in dic:
                    dic[v[i]] = {}
                if i not in dic[v[i]]:
                    dic[v[i]][i] = 0
                dic[v[i]][i] += 1

        # custom comparator
        def compare(a, b, size):
            for i in range(size):
                if i in a[1] and i not in b[1]:
                    return -1
                elif i not in a[1] and i in b[1]:
                    return 1
                elif i not in a[1] and i not in b[1]:
                    continue
                else:
                    if a[1][i] > b[1][i]:
                        return -1
                    elif a[1][i] < b[1][i]:
                        return 1
                    else:
                        continue
            return 0

        sorted_dic = sorted(dic.items(), cmp=lambda a, b: compare(a, b, len(votes[0])))
        res = [x[0] for x in sorted_dic]
        return "".join(res)

test = Solution()
print test.rankTeams(["ABC","ACB","ABC","ACB","ACB"])
print test.rankTeams(["WXYZ","XYZW"])
print test.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"])