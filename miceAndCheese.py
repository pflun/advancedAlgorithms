class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        reward = []
        for i in range(len(reward1)):
            reward.append([reward1[i], reward2[i]])
        # custom comparator
        def compare(a, b):
            if a[0] - a[1] > b[0] - b[1]:
                return -1
            elif a[0] - a[1] < b[0] - b[1]:
                return 1
            return 0

        sorted_reward = sorted(reward,  cmp=lambda a, b: compare(a, b))
        res = 0
        for i in range(k):
            res += sorted_reward[i][0]
        for i in range(k, len(sorted_reward)):
            res += sorted_reward[i][1]
        return res
