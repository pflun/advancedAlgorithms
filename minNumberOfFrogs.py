class Solution(object):
    def minNumberOfFrogs2(self, croakOfFrogs):
        c = r = o = a = k = 0
        watermark = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
                watermark = max(watermark, c - k)
            elif ch == 'r':
                r += 1
            elif ch == 'o':
                o += 1
            elif ch == 'a':
                a += 1
            elif ch == 'k':
                k += 1
            else:
                return -1
            if not c >= r >= o >= o >= k:
                return -1
        return watermaek if c == r == o == a == k else -1

    # TLE
    def minNumberOfFrogs(self, croakOfFrogs):
        res = 0
        queue = []
        for i in range(len(croakOfFrogs)):
            if len(queue) == 0:
                if croakOfFrogs[i] != 'c':
                    return -1
                queue.append(croakOfFrogs[i])
                continue
            for j in range(len(queue)):
                # print queue, queue[j], croakOfFrogs[i]
                if croakOfFrogs[i] == 'c':
                    queue.append(croakOfFrogs[i])
                    break
                if self.match(queue[j], croakOfFrogs[i]):
                    if croakOfFrogs[i] == 'k':
                        del queue[j]
                    else:
                        queue[j] += croakOfFrogs[i]
                    break
            res = max(res, len(queue))
        if len(queue) != 0:
            return -1
        return res

    def match(self, tmp, c):
        if len(tmp) == 1 and c == 'r':
            return True
        elif len(tmp) == 2 and c == 'o':
            return True
        elif len(tmp) == 3 and c == 'a':
            return True
        elif len(tmp) == 4 and c == 'k':
            return True
        return False

test = Solution()
print test.minNumberOfFrogs("croakcroak")
print test.minNumberOfFrogs("crcoakroak")
print test.minNumberOfFrogs("croakcrook")
print test.minNumberOfFrogs("croakcroa")
print test.minNumberOfFrogs("crocracokrakoak")