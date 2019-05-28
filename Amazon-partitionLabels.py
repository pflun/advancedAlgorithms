# -*- coding: utf-8 -*-
# You are working on developing a movie with Amazon Video and want to devise an application to easily break up individual shots in a video into scenes.
# There is already an algorithm that breaks the video up into shots (short sequences from a particular camera angle) and labels them.
#
# Write a function which will partition a sequence of labels into minimal subsequences so that no labels appear in more than one subsequence.
# The output should be the length of each subsequence.
#
# Input:
# The input to the function/method consists of an argument - inputList, a list of characters representing the sequence of shots.
#
# Output:
# Return a list of integers representing the length of each scene, in the order in which it appears in the given sequence of shots.
#
# Example:
#
# Input:
# inputList = [a,b,a,b,c,b,a,c,a,d,e,f,e,g,d,e,h,i,j,h,k,l,i,j]
# Output:
# [9, 7, 8]
# Explanation:
# The correct partitioning is:
# a,b,a,b,c,b,a,c,a,/d,e,f,e,g,d,e,/h,i,j,h,k,l,i,j
# To ensure that no label appears in more than one subsequence, subsequences are as small as possible, and subsequences partition the sequence.
# The length of these subsequences are 9, 7 and 8.
# 遍历一次string用一个map记录每个character出现的次数。重新遍历 一次string, 用target sum记录当前partition里所有character应该出现的总次数，
# 如果当前的character是第一次出现，就把 target sum加上对应char出现的次数，同时用begin和end记录当前的partition,
# 如果partition的size等于target sum 就算找到 一个partition.

# 另一种解法：https://www.youtube.com/watch?v=s-1W5FDJ0lw
# lastIndex记录每个字符最后出现的次数，随着扫描，end指针可能会extend（根据lastIndex）。
# 当扫描的 i == end 时，找到一个partition，start = end + 1

class Solution(object):
    def partitionlabels(self, labels):
        dic = {}
        res = []
        sum = 0
        tmp = set()
        for label in labels:
            dic[label] = dic.get(label, 0) + 1

        left = 0
        right = 0
        while right < len(labels):
            if labels[right] not in tmp:
                tmp.add(labels[right])
                sum += dic[labels[right]]

            if right - left + 1 == sum:
                res.append(right - left + 1)
                sum = 0
                tmp = set()
                left = right + 1
            right += 1

        return res


test = Solution()
print test.partitionlabels(['a','b','a','b','c','b','a','c','a','d','e','f','e','g','d','e','h','i','j','h','k','l','i','j'])

# Solution 2:
# 首先遍历一遍，存下来所有的字符第一次和最后一次出现的位置，然后就等于有一个vector<Interval>；然后merge interval来做。
# 比如 abcfabde， 就是 ：
# a: [0,4];
# b: [1,5];
# c: [2,2];
# f: [3,3];
# d:[6,6];
# e:[7,7];
# merge 以后是:
# [0,5] [6,6] [7,7]
# abcfab| d |e