class Solution(object):
    def groupAnagrams(self, strs):
        str_dist = {}
        for i in xrange(len(strs)):
            temp = ''.join(sorted(strs[i]))
            str_dist[temp] = str_dist.get(temp, []) + [strs[i]]
        return [sorted(item) for item in str_dist.values()]

    def groupAnagrams2(self, strs):
        dic = {}
        res = []

        # Sorted str => str, ie: aet => tea
        for str in strs:
            tmp = ''.join(sorted(str))
            if tmp not in dic:
                dic[tmp] = [str]
            else:
                dic[tmp].append(str)

        for key, val in dic.items():
            res.append(val)

        return res

test = Solution()
print test.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])