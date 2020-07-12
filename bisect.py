# https://docs.python.org/2/library/bisect.html
from _bisect import *

def binarySearch(arr, target):
    'Locate the leftmost value exactly equal to x'
    idx = bisect_left(arr, target)
    if idx != len(arr) and arr[idx] == target:
        return idx

print binarySearch([1,2,3,4,5,6,7,8], 7)

# from sortedcontainers import SortedDict
# dic = SortedDict()
# dic[2] = 2
# dic[5] = 5
# dic[3] = 3
# dic[1] = 1
# for k in dic.keys():
#     print k

# first larger than threshold
l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print bisect(l, 55)
print bisect(l, 99)
print bisect(l, 100)
print bisect(l, 101)