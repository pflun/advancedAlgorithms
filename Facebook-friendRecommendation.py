# -*- coding: utf-8 -*-
# 模拟fb好友推荐。给一个function，可以return某一个id的所有好友。需要完成一个function
# 就是input 一个id，output list of friends of friends, ordered by number of mutual
#  friends.
#
# ANS: 大概就是新建一个class，有id和number of mutual friends field,
# 然后override hash function(保证不用重新计算已经算过mutual friends的id)。
# 在immediate friends list里面iterate，然后把每一个朋友的朋友和他们的mutual friend number
# 加入list。最后写一个comparator，用collection.sort 按照mutual friends排序就好
class Solution(object):
    def friendRecommendation(self, id, graph):
        dic = {}
        for f in graph[id]:
            for fof in graph[f]:
                if fof == id:
                    continue
                if fof in graph[id]:
                    dic[fof] = dic.get(fof, 0) + 1
        res = [(key, value) for (key, value) in dic.items()]
        return sorted(res, key=lambda x: x[1])

    def findFriends(self, id):
        return []