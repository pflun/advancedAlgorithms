# Below code works but not for Closed  intervals, need debug in else condition
class Solution(object):
    def intervalIntersection2(self, A, B):
        res = []
        p1 = 0
        p2 = 0
        while p1 < len(A) and p2 < len(B):
            start = max(A[p1][0], B[p2][0])
            end = min(A[p1][1], B[p2][1])

            # found overlap
            if end >= start:
                res.append([start, end])

            # move pointer with smaller end
            if A[p1][1] == end:
                p1 += 1
            if B[p2][1] == end:
                p2 += 1
        return res

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
print test.intervalIntersection2([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])