# import time
class TimeMap(object):

    def __init__(self):
        self.dic = {}

    def set(self, key, value, timestamp):
        # timestamp = time.time()
        self.dic[key] = self.dic.get(key, []) + [[timestamp, value]]

    def get(self, key, timestamp):
        if key not in self.dic or not self.dic[key]:
            return ""
        arr = self.dic[key]
        n = len(arr)

        left = 0
        right = n

        while left < right:
            mid = (left + right) / 2
            # target at left side, move right
            if arr[mid][0] > timestamp:
                right = mid
            elif arr[mid][0] <= timestamp:
                left = mid + 1

        return "" if right == 0 else arr[right - 1][1]

test = TimeMap()
print test.set(1, 1, 1)
print test.set(1, 2, 2)
print test.get(1, 1)
print test.get(1, 2)
print test.get(1, 3)