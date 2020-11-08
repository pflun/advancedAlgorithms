# Given a pattern and a string input - find if the string follows the same pattern and return true or false.
# Pattern : "abab", input: "redblueredblue" should return true.
# Pattern: "aaaa", input: "asdasdasdasd" should return true.
# Pattern: "aabb", input: "xyzabcxzyabc" should return false.
# dfs + backtracking, dic = {potential mapping between char in pattern and substr in str}

class Solution(object):
    def isMatch(self, str, pat):
        return self.helper(str, i, pat, j, {})

    def helper(self, str, i, pat, j, dic):
        # Both end
        if i == len(str) and j == len(pat):
            return True
        # Only one pointer reach to the end
        if i == len(str) or j == len(pat):
            return False
        currP = pat[j]
        # exist pattern in dic
        if currP in dic:
            currS = dic[currP]
            # check if next substr match currS
            if i + len(currS) > len(str) or str[i:i + len(currS)] != currS:
                return False
            else:
                # good it matched, we can continue
                return self.helper(str, i + len(currS), pat, j + 1, dic)
        else:
            # pattern not exist, create new mapping
            for k in range(i, len(str)):
                dic[currP] = str[i:k + 1]
                if self.helper(str, k + 1, pat, j + 1, dic):
                    return True
                del dic[currP]
        return False