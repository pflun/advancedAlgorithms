class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        res = 0
        idx = 0
        if ruleKey == 'type':
            idx = 0
        elif ruleKey == 'color':
            idx = 1
        elif ruleKey == 'name':
            idx = 2
        for it in items:
            if it[idx] == ruleValue:
                res += 1

        return res

test = Solution()
print test.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")
print test.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone")