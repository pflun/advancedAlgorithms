# -*- coding: utf-8 -*-
# A bot is an id that visit the site m ‍‍‍‍‍‌‍‍‍‌‍‍‍‍‌‍times in the last n seconds,
# given a list of logs with id and time sorted by time, return all the bots's id
# Map<user id, count of login event in timeframe> + Queue<Event(user id, timestamp)>.
# 只存一个timeframe(比如60s)里面的所有event. 每当有新的timestamp扫描进来的时候, 移除queue里面所有超时的event, 同时更新map里面userid对应的count
# 这题像design Hit Counter
class Log(object):
    def __init__(self, id, time):
        self.id = id
        self.time = time

class Solution(object):
    def getBots(self, logs, n, m):
        dic = {}
        res = set()
        for l in logs:
            id = l.id
            time = l.time
            if id in res:
                continue
            if id not in dic:
                dic[id] = [time]
            else:
                # 移除超时
                while len(dic[id]) > 0 and time - dic[id][0] > n:
                    dic[id].pop(0)
                dic[id].append(time)
            if len(dic[id]) >= m:
                res.add(id)
        return res