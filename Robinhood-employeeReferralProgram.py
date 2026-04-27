# https://leetcode.com/discuss/post/7041056/robinhood-round-1-interview-question-by-l7o51/
import heapq

class Solution:
    def __init__(self):
        # self.dic stores the parent of each user in the Union Find tree. 
        # Example: if A refers B, self.dic['B'] = 'A'
        # It's used to quickly lookup "who is the root referrer for this component?"
        self.dic = {}
        
        # self.size stores the total number of users in a referral component (including the root referrer themselves).
        # It maps the root user to the size of their entire down-line subtree.
        # Example: if A refers B and B refers C, self.size['A'] = 3
        self.size = {}

    def find(self, x):
        if x not in self.dic:
            self.dic[x] = x
            
        parent = self.dic[x]
        while parent != self.dic[parent]:
            parent = self.dic[parent]
        return parent

    def union(self, master, branch):
        fa_master = self.find(master)
        fa_branch = self.find(branch)
        
        if fa_master != fa_branch:
            self.dic[fa_branch] = fa_master
            self.size[fa_master] = self.size.get(fa_master, 1) + self.size.get(fa_branch, 1)

    def getTop3Referrals(self, rh_users, new_users):
        # 1. Process backwards
        for i in range(len(rh_users) - 1, -1, -1):
            master = rh_users[i]
            branch = new_users[i]
            self.union(master, branch)
            
        # 2. Add eligible users to heap
        heap = []
        for user, total_size in self.size.items():
            referrals = total_size - 1
            if referrals > 0:
                # (-referrals, user) ensures max-heap for referrals and min-heap for names
                heap.append((-referrals, user))
                
        # heapify runs in O(N) time
        heapq.heapify(heap)
        
        # 3. Pop the top 3 elements (or fewer if there are less than 3 users)
        res = []
        for _ in range(min(3, len(heap))):
            neg_referrals, user = heapq.heappop(heap)
            res.append(user + '' + str(-neg_referrals))
            
        return res

test = Solution()
rh_users = ["A", "B", "C"]
new_users = ["B", "C", "D"]
print(test.getTop3Referrals(rh_users, new_users))
