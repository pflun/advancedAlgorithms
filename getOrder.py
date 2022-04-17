import heapq
class Solution(object):
    def getOrder(self, tasks):
        tasks_copy = []
        for i in range(len(tasks)):
            tasks_copy.append([tasks[i][0], tasks[i][1], i])
        tasks_copy.sort()
        time = tasks_copy[0][0]
        heap = []
        heapq.heapify(heap)
        res = []
        idx = 0
        while len(res) < len(tasks_copy):
            if idx < len(tasks_copy):
                time = max(time, tasks_copy[idx][0])
            while idx < len(tasks_copy):
                if tasks_copy[idx][0] <= time:
                    heapq.heappush(heap, (tasks_copy[idx][1], tasks_copy[idx][2]))
                    idx += 1
                else:
                    break
            if heap and time >= tasks_copy[heap[0][1]][0]:
                currTime, currIdx = heapq.heappop(heap)
                res.append(currIdx)
                time += currTime
            elif heap and time < tasks_copy[heap[0][1]][0]:
                currTime, currIdx = heapq.heappop(heap)
                res.append(currIdx)
                time = currTime
        return res

test = Solution()
print test.getOrder([[1,2],[2,4],[3,2],[4,1]])
print test.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]])
print test.getOrder([[4,1],[3,1]])
print test.getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]) # [6,1,2,9,4,10,0,11,5,13,3,8,12,7]