# Below code works but not for Closed  intervals, need debug in else condition
class Solution(object):
    def intervalIntersection(self, A, B):
        starts = []
        ends = []
        res = []

        for a in A:
            starts.append(a[0])
            ends.append(a[1])
        for b in B:
            starts.append(b[0])
            ends.append(b[1])
        starts.sort()
        ends.sort()

        i = 0
        j = 0
        curr = 0
        tmp = []

        while i < len(starts):
            print i, j, starts, ends
            if starts[i] < ends[j]:
                curr += 1
                if curr == 2 and len(tmp) == 0:
                    tmp.append(starts[i])
                i += 1
            elif starts[i] > ends[j]:
                curr -= 1
                if curr < 2 and len(tmp) == 1:
                    tmp.append(ends[j])
                    res.append([tmp[0], tmp[1]])
                    tmp = []
                j += 1
            else:
                if curr == 2 and len(tmp) == 0:
                    tmp.append(starts[i])
                i += 1
                j += 1
        if len(tmp) == 1:
            res.append([tmp[0], ends[-1]])

        return res

test = Solution()
print test.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])