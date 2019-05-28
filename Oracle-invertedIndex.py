# -*- coding: utf-8 -*-
# 类似recommendation算法。给如下的user list和每个user看过的movie的list
#              u1: m1, m2, m3, m4, m5, m2
#              u2: m4, m3, m2
# 先讨论了比如u3看了m4，怎么返回一个推荐给它的movie，
# 然后做了一个加了很多限制变简单化的实现。
class Solution(object):
    def invertedIndex(self, movieList, newList):
        inverted = {}
        # inverted: movie => [user1, user2]
        for key, val in movieList.items():
            for v in val:
                if v not in inverted:
                    inverted[v] = [key]
                else:
                    if key not in inverted[v]:
                        inverted[v].append(key)

        for key, val in newList.items():
            # get movies from new user list
            for v in val:
                # if the movie from new user only has one other user watched
                if len(inverted[v]) == 1:
                    recommend = movieList[inverted[v][0]]
                    return recommend
                # if several other users watched this movie
                else:
                    # 取出第一个list，准备与后面的list取并集
                    recommend = movieList[inverted[v][0]]
                    for i in range(1, len(inverted[v])):
                        # 多个list找并集
                        recommend = set(movieList[inverted[v][i]]) & set(recommend)

        return list(recommend)


test = Solution()
print test.invertedIndex({'u1': ['m1','m2','m3','m4','m5','m2'], 'u2': ['m4','m3','m2']}, {'u3': ['m4']})