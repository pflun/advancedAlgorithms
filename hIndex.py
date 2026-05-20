# -*- coding: utf-8 -*-
class Solution(object):
    # 空间换时间
    def hIndex2(self, citations):
        n = len(citations)
        # 建 n + 1 个水桶，因为 H-Index 的最大可能值就是 n (即论文总数)
        buckets = [0] * (n + 1)
        
        # 1. 遍历所有论文，将其扔进对应的水桶中
        # buckets[i] 里面存的是：“在这个科学家的所有论文中，引用次数【恰好】等于 i 的论文的数量”
        # 这个for loop纯粹是避免创建巨大的10,000 list
        for c in citations:
            if c >= n:
                # 关键截断：如果引用量大于等于 n，统统算作 n
                # 因为即使引用量上亿，这辈子的 H-Index 也不可能超过总论文数 n
                buckets[n] += 1
            else:
                buckets[c] += 1
                
        papers = 0
        # 2. 从最高可能的 H-Index (n) 开始往下倒序遍历
        for h in range(n, -1, -1):
            # 累加引用量大于等于当前 h 的所有论文数
            papers += buckets[h]
            # 一旦累加的论文总数达到了当前的 h，说明吹牛成功，找到了最大边界！
            if papers >= h:
                return h
                
        return 0

    def hIndex(self, citations):
        citations.sort()
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0
test = Solution()
print test.hIndex2([3, 0, 6, 1, 5])
