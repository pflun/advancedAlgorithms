import heapq
class Solution(object):
    def assignTasks(self, servers, tasks):
        res = [0 for _ in range(len(tasks))]
        # Available servers [weight, idx]
        heap = []
        # Occupied servers [finishing time, weight, idx]
        occupied = []
        heapq.heapify(heap)
        heapq.heapify(occupied)
        for i in range(len(servers)):
            heapq.heappush(heap, [servers[i], i])
        t = 0
        for i in range(len(tasks)):
            # update current time
            t = max(t, i)
            # move free servers at t time to available heap
            while occupied and occupied[0][0] <= t:
                free = heapq.heappop(occupied)
                heapq.heappush(heap, [free[1], free[2]])
            # if not heap, then no free servers, must wait til earliest occupied server become free
            # so t fast forward to the earliest occupied server finishing time, then use this server don't put in heap
            if heap:
                curr = heapq.heappop(heap)
                res[i] = curr[1]
                heapq.heappush(occupied, [t + tasks[i], curr[0], curr[1]])
            else:
                next = heapq.heappop(occupied)
                t = next[0]
                res[i] = next[2]
                heapq.heappush(occupied, [t + tasks[i], next[1], next[2]])
        return res

test = Solution()
print test.assignTasks([3,3,2], [1,2,3,2,1,2])
print test.assignTasks([5,1,4,3,2], [2,1,2,4,5,2,1])
print test.assignTasks([10,63,95,16,85,57,83,95,6,29,71], [70,31,83,15,32,67,98,65,56,48,38,90,5])