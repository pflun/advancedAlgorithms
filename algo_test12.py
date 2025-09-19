from collections import OrderedDict
class Solution(object):
    def addStrings(self, num1, num2):
        res = 0
        i = 0
        pos = 1
        num1 = num1[::-1]
        num2 = num2[::-1]
        while i < len(num1) and i < len(num2):
            remain = int(num1[i]) + int(num2[i])
            res += remain * pos
            pos *= 10
            i += 1
        if i < len(num1):
            for j in range(i, len(num1)):
                res += int(num1[j]) * pos
        elif i < len(num2):
            for j in range(i, len(num2)):
                res += int(num2[j]) * pos
        return res

    def accept(self, n):
        return True if n < 8 else False

    def helper(self, arr):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (low + high) / 2
            print mid
            if self.accept(arr[mid]):
                low = mid
            else:
                high = mid - 1
        return arr[low] if self.accept(arr[low]) else None

test = Solution()
print test.addStrings("125", "45")
print test.helper([1,3,7,9,10])
print sorted(['/home/joe', '/application', '/home/joe/music/baba'])
print int('10', 16)

# add dict as value in a dict
dicP = {}
dicC = {'a': 57}
dicP['A'] = dicC
print dicP['A']['a']

def getOnes(n):
    binary = bin(n)
    cnt = 0
    for b in str(binary):
        if b == "1":
            cnt += 1
    return cnt

mylist = [100,1,2,3,4,5]

mylist.sort(key=lambda x: getOnes(x))
print mylist
print 65535/1000, 65535%1000, 65535%1000/1000

ordDic = OrderedDict()
ordDic[2] = 2
ordDic[5] = 5
ordDic[3] = 3
ordDic[1] = 1
for k in ordDic.keys():
    print k
# import numpy
# mtx = numpy.array([
#   [1, 3, 5, 7],
#   [10, 11, 16, 0],
#   [23, 0, 34, 0],
#   [51, 52, 54, 40]
# ])
# print mtx[:2, :2]
# dp = {}
# dp[1, 2] = '12'
# print dp.get(1, 2)

def solution(angles):
    # Type your solution here
    cnt = 0
    for a in angles:
        if a == '<':
            cnt += 1
        elif a == '>':
            cnt -= 1
        if cnt < 0:
            cnt = 0
    right = cnt
    cnt = 0
    for a in angles[::-1]:
        if a == '<':
            cnt -= 1
        elif a == '>':
            cnt += 1
        if cnt < 0:
            cnt = 0
    left = cnt
    res = ''
    for _ in range(left):
        res += '<'
    res += angles
    for _ in range(right):
        res += '>'
    return res
print solution("><<><")
unsorted = [[2,6], [3,2], [2,5]]
unsorted.sort()
print unsorted
import heapq
print heapq.nlargest(2, [3, 5, 7, 9])

class Player(object):
    def __init__(self, dir):
        self.directions = set(['up', 'down', 'left', 'right'])
        self.dir = None
        if dir in self.directions:
            self.dir = dir
        else:
            raise ValueError('wrong dir')

# p2 = Player('up')
# print p2.dir
# p1 = Player('upppp')

print [m for m in None]