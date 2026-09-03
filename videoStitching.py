# -*- coding: utf-8 -*-
class Solution:
    def videoStitching(self, clips, T):
        # 按起点从小到大排序
        clips = sorted(clips)
        # start, end 代表你【当前这一步】能合法出发的起点区间
        # 初始时，你只能从 0 开始。
        start, end = 0, 0
        cnt = 0
        idx = 0
        while start <= end:
            cnt += 1
            # newend 是我们在接下来的候选片段中，能找到的“最远到达距离”
            newstart, newend = end + 1, end
            # 遍历所有能够和当前区间 [start, end] 拼上的片段
            # 条件是：它的起点必须 <= 当前的 end (这样才不会有缝隙)
            while idx < len(clips) and start <= clips[idx][0] <= end:
                # 在所有合法的片段中，贪心地记录下那个能伸得最远的终点
                newend = max(newend, clips[idx][1])
                # 如果这个最远的终点已经覆盖了目标 T
                if newend >= T:
                    return cnt
                idx += 1
            # 我们刚才挑了一个最猛的片段，现在我们的覆盖范围更新为了新边界。
            # 下一轮能挑的片段，起点最远不能超过 newend。
            start, end = newstart, newend
        return -1