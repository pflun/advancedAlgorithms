class Solution(object):
    def compareVersion(self, version1, version2):
        if not version1 or not version2:
            return 0
        v1 = version1.split('.')
        v2 = version2.split('.')
        # in case version1 = '1', v1 = ['1']
        if len(v1) == 1:
            v1.append(0)
        if len(v2) == 1:
            v2.append(0)
        # Compare
        i = 0
        while i < len(v1) and i < len(v2):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            i += 1

        if i > len(v1):
            return -1
        else:
            return 1

test = Solution()
print test.compareVersion('7.5.12.4', '7.5.3')