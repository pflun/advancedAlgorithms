# Task Scheduler
# Greedy, https://www.youtube.com/watch?v=YCD_iYxyXoo
# ans = (maxfaq - 1) * (n + 1) + p, p is how many elements that faq == A (assume A has highest faq)
# tasks = ["A","A","A","B","B","B"], n = 2 ==> (3 - 1) * (2 + 1) + 2 = 8

class Solution(object):
    def leastInterval(self, tasks, n):
        dic = {}
        for task in tasks:
            dic[task] = dic.get(task, 0) + 1

        maxfaq = 0
        for key, val in dic.items():
            maxfaq = max(maxfaq, val)

        p = 0
        for key, val in dic.items():
            if val == maxfaq:
                p += 1

        # A B C... A B idle... A
        res = (maxfaq - 1) * (n + 1) + p

        # Special case: tasks > res, more tasks than Greedy solution needed (no idle need to use)
        return max(len(tasks), res)

test = Solution()
print test.leastInterval(["A","A","A","B","B","B"], 2)