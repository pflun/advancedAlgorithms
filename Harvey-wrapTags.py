class Solution(object):
    def wrapTags(self, document, sources):
        intervals = []
        for source in sources:
            start = 0
            while True:
                start = document.find(source, start)
                if start == -1:
                    break
                end = start + len(source)
                intervals.append([start, end, source])
                start += 1
        # Merge Intervals
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # empty merged or (no overlap && gap is not space)
            if len(merged) == 0 or (merged[-1][1] < interval[0] and document[merged[-1][1]:interval[0]] != " "):
                merged.append([interval[0], interval[1], [interval[2]]])
            else:
                # update last interval
                merged[-1][1] = max(merged[-1][1], interval[1])
                merged[-1][2].append(interval[2])
        res = []
        idx = 0
        for start, end, source_list in merged:
            res.append(document[idx:start])
            res.append("<yellow>")
            res.append(document[start:end])
            res.append("</yellow>")
            idx = end
        res.append(document[idx:])
        return "".join(res)

test = Solution()
print test.wrapTags("abc foo bar foo", ["foo", "bar"])
print test.wrapTags("aaaa", ["aa"])
print test.wrapTags("hello world", ["x"])
print test.wrapTags("ababa", ["aba", "bab"])
print test.wrapTags("foo xxx bar yyy foo", ["foo", "bar"])
print test.wrapTags("hello world hello universe", ["hello world", "world hello", "hello universe"])
