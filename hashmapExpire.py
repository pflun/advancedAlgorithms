# -*- coding: utf-8 -*-
# 面试官是个安卓组的小姐姐，45分钟，感觉答得一般，求过o 0
# Create a map with expiring entries:
# Example
# 12:00:00 - put(10, 25, 5000)
# 12:00:04 - get(10) -> 25
# 12:00:06 - get(10) -> null
#
# 思路：两个hash map，一个记录key，value pair，一个记录key的过期时间，get的时候检查key是否过期，如果过期了，删除key返回null
# Put方法有三个参数，除了key，value还有个duration
import time
class hashmapExpire(object):
    def __init__(self, ):
        self.dic = {}
        self.expire = {}

    def put(self, key, value, expire):
        self.dic[key] = value
        self.expire[key] = time.time() + expire

    def get(self, key):
        if key in self.expire:
            tmp = self.expire[key]
            if tmp >= time.time():
                return self.dic[key]
            else:
                self.dic.pop(key)
                self.expire.pop(key)
                return None
        else:
            return None

test = hashmapExpire()
test.put(10, 25, 5)
print test.get(10)
time.sleep(6)
print test.get(10)