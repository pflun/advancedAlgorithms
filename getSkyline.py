# -*- coding: utf-8 -*-
# 扫描线
import heapq
class Solution(object):
    def getSkyline(self, buildings):
        # 对于一个 building, 他由 (l, r, h) 三元组组成, 我们可以将其分解为两种事件:
        #     1. 在 left position, 高度从 0 增加到 h(并且这个高度将持续到 right position);
        #     2. 在 right position, 高度从 h 降低到 0.
        # 对于在 right position 高度降为 0 的 event, 它的持续长度时无效的
        # 由于需要从左到右触发 event, 所以按 postion 对 events 进行排序
        # 并且, 对于同一 positon, 我们需要先触发更高 h 的事件, 先触发更高 h 的事件后, 那么高的 h 相比于低的 h 会占据更高的 skyline
        # 所以, event 不仅需要按第一个元素 position 排序, 在 position 相同时, 第二个元素 h 也是必须有序的
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()

        # res 记录了 `key point` 的结果: [x, h]
        # 同时 res[-1] 处的 `key point` 代表了在下一个 event 触发之前, 一直保持的最高的 skyline
        # live 记录了对于一条高为 h 的 skyline, 他将持续到什么 position 才结束: [h, endposition]
        # res: result, [x, height]
        # hp: heap, [-height, ending position]
        res = [[0, 0]]
        hp = [(0, float("inf"))]

        for l, neg_h, r in events:
            # 触发 event 时, 首先要做的就是清除已经到 endposition 的 skyline
            # hp: [h, endposition]
            # 如果当前 position 大于等于了 hp 中的 endposition, 那么该 skyline 会被清除掉
            # 由于在有 high skyline 的情况下, low skyline 不会有影响, 因此, 只需要按从高到低的方式清除 skyline, 直到剩下一个最高的 skyline 并且它的 endposition 大于当前 position
            while l >= hp[0][1]:
                heapq.heappop(hp)

            # 对于高度增加到 h 的时间(neg_h < 0), 我们需要添加一个 skyline, 他将持续到 r 即 endposition
            if neg_h:
                heapq.heappush(hp, (neg_h, r))

            # 由于 res[-1][1] 记录了在当前事件触发之前一直保持的 skyline
            # 如果当前事件触发后 skyline 发生了改变
            #     1. 来了一条新的高度大于 h 的 skyline
            #     2. res[-1] 中记录的 skyline 到达了 endposition
            # 这两种事件都会导致刚才持续的 skyline 与现在最高的 skyline 不同; 同时, `key point` 产生了, 他将被记录在 res 中
            if res[-1][1] != -hp[0][0]:
                res.append([l, -hp[0][0]])

        return res[1:]

test = Solution()
print test.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ])