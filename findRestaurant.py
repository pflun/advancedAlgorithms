class Solution(object):
    def findRestaurant(self, list1, list2):
        dic = {}
        candidates = []
        res = []
        # Restaurant => list(index)
        for i in range(len(list1)):
            dic[list1[i]] = [i]
        for j in range(len(list2)):
            if list2[j] in dic:
                dic[list2[j]].append(j)
            else:
                dic[list2[j]] = [j]

        # sum(indexs) => Restaurant
        for key, val in dic.items():
            if len(val) == 2:
                candidates.append([val[0] + val[1], key])
        candidates.sort()
        # After sort, slice start to possible tie
        for k in range(len(candidates)):
            if k < len(candidates) - 1 and candidates[k][0] != candidates[k + 1][0]:
                candidates = candidates[0:k + 1]

        for r in candidates:
            res.append(r[1])

        return res

test = Solution()
print test.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])