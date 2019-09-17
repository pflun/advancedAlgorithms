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