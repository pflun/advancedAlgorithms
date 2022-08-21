class Solution(object):
    def distributeCookies(self, cookies, k):
        self.res = float('inf')
        fair = [0 for _ in range(k)] # cookies for each child

        # next cookie index
        def dfs(next):
            if next == len(cookies):
                self.res = min(self.res, max(fair))
                return
            # pruning
            if self.res <= max(fair):
                return
            # try to assign current cookie to each child and move on to next cookie
            for i in range(k):
                fair[i] += cookies[next]
                dfs(next + 1)
                fair[i] -= cookies[next]
        dfs(0)
        return self.res

test = Solution()
print test.distributeCookies([8,15,10,20,8], 2)
print test.distributeCookies([6,1,3,2,2,4,1,2], 3)