class Solution(object):
    def largestWordCount(self, messages, senders):
        dic = {}
        res = 0
        largest_cnt = 0
        for i in range(len(messages)):
            sender = senders[i]
            cnt = len(messages[i].split(' '))
            dic[sender] = dic.get(sender, 0) + cnt

        for k, v in dic.items():
            if v > largest_cnt:
                res = k
                largest_cnt = v
            elif v == largest_cnt:
                if k > res:
                    res = k
        return res

test = Solution()
print test.largestWordCount(["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], ["Alice","userTwo","userThree","Alice"])
print test.largestWordCount(["How is leetcode for everyone","Leetcode is useful for practice"], ["Bob","Charlie"])