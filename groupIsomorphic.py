# Given an array with strings, group the isomorphic strings into groups.
# For example:
# Given ['aba', 'zzz','dccb', 'ded', 'ccc', 'aaa', 'cbba']
# Return [ [ 'zzz', 'ccc', 'aaa' ], [ 'aba', 'ded' ], [ 'dccb', 'cbba' ] ]

class Solution:
    def groupIsomorphic(self, arr):
        hash = {}
        res = []
        for string in arr:
            dic = {}
            for i in range(len(string)):
                if string[i] in dic:
                    dic[string[i]].append(str(i))
                else:
                    dic[string[i]] = [str(i)]

            # build hash looks like: 0#12#3#, 02#1#
            hashval = ''
            for li in sorted(dic.values()):
                tmp = ''.join(li)
                hashval = hashval + tmp + '#'

            if hashval in hash:
                hash[hashval].append(string)
            else:
                hash[hashval] = [string]

        for key,val in hash.items():
            res.append(val)

        return res

# dic = {'a': ['0', '2'], 'b': ['1']} ==> hash['02#1#'] = ['aba', 'ded']
test = Solution()
print test.groupIsomorphic(['aba', 'zzz','dccb', 'ded', 'ccc', 'aaa', 'cbba'])