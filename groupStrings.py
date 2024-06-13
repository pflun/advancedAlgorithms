# Use (diff1, diff2) or (1, 1) as key, cannot use "11" as key because it will conflict with diff eleven
# {
#      (1, 1): ['abc', 'bcd', 'xyz'],
#   (2, 2, 1): ['acef'],
#       (25,): ['az', 'ba'],
#          (): ['a', 'z']
# }
class Solution(object):
    def groupStrings(self, strings):
        dic = {}
        for s in strings:
            if len(s) == 1:
                dic['single'] = dic.get('single', []) + [s]
            else:
                key = ()
                for i in range(len(s) - 1):
                    key += ((ord(s[i + 1]) - ord(s[i])) % 26, )
                dic[key] = dic.get(key, []) + [s]
        res = []
        for v in dic.values():
            res.append(v)
        return res

test = Solution()
print test.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"])
print test.groupStrings(["a"])
print test.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z","al"])