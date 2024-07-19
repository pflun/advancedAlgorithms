class Solution(object):
    def minWindow2(self, s, t):
        s_count, t_count = {}, {}
        l, r = 0, 0
        results = []
        for i in t:
            t_count[i] = t_count.get(i, 0) + 1

        while r <= len(s) - 1:
            # Find valid window
            s_count[s[r]] = s_count.get(s[r], 0) + 1
            r += 1
            if not self.include(s_count, t_count):
                continue

            # Minimize this window
            while l < r:
                s_count[s[l]] -= 1
                l += 1
                if self.include(s_count, t_count):
                    continue
                results.append(s[l - 1:r])
                break

        # Return result
        if not results:
            return ""
        return min(results, key=len)

    def include(self, s_count, t_count):
        for k, v in t_count.items():
            if k not in s_count or s_count[k] < v:
                return False
        return True

    # Two pointer: dic count char => faq, right.found() dic[char]++, when left++, dic[left]--. if counter == len(t): res=min(res, len(curr))
    # https://www.youtube.com/watch?v=63i802XLgOM
    def minWindow(self, s, t):
        if len(s) == 0 or len(t) == 0 or len(t) > len(s):
            return ""
        # a, a
        elif len(t) == 1 and len(s) == 1 and t == s:
            return t

        dicS = {}
        dicT = {}
        counter = 0
        res = None

        for i in t:
            dicT[i] = dicT.get(i, 0) + 1

        # move left to the very first match char
        for left in range(len(s)):
            if s[left] in t:
                break

        if left == len(s) - 1:
            # only match the last char
            if t == s[left]:
                return t
            # no match at all
            else:
                return ""

        for right in range(left, len(s)):
            if s[right] in t:
                # s[right] is not redundant
                if s[right] not in dicS or dicS[s[right]] < dicT[s[right]]:
                    counter += 1
                    dicS[s[right]] = dicS.get(s[right], 0) + 1
                    # match
                    if counter == len(t):
                        if res == None:
                            res = s[left:right + 1]
                        else:
                            if len(res) > len(s[left:right + 1]):
                                res = s[left:right + 1]

                        # left redundant
                        if dicS[s[left]] > dicT[s[left]]:
                            dicS[s[left]] = dicS.get(s[left]) - 1
                        # left Not redundant
                        else:
                            counter -= 1
                            dicS[s[left]] = dicS.get(s[left]) - 1

                        # move left to next match char
                        for left in range(left + 1, len(s)):
                            if s[left] in t:
                                # print s[left], s[right], dicS[s[left]]
                                break

                # redundant
                else:
                    dicS[s[right]] = dicS.get(s[right], 0) + 1

        return res

test = Solution()
print test.minWindow2("ADOBECODEBANC", "ABC")