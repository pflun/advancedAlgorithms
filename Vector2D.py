# -*- coding: utf-8 -*-
class Vector2D(object):
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.x = 0
        self.y = 0

    def next(self):
        if self.hasNext():
            res = self.vec2d[self.x][self.y]
            self.y += 1
            return res
        else:
            return -1

    def hasNext(self):
        # 防止x出界，y如果到每行最后一个x就挪到下一行
        while self.x < len(self.vec2d) and self.y == len(self.vec2d[self.x]):
            self.x += 1
            self.y = 0
        return True if self.x < len(self.vec2d) else False

test = Vector2D([
  [1,2],
  [3],
  [4,5,6]
])
print test.hasNext()
print test.next()
print test.next()
print test.hasNext()
print test.next()