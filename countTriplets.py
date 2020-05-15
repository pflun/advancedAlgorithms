# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=30A0Z2KDvaA
class Solution(object):
    # a = b 所以 a ^ b = 0
    # i to j == j to k 所以从i ^ k为0，所以找preXOR[k] - preXOR[i] = 0的点，note: 意味着j可以取i到k中间任意值，所以要都加上 res += k - i
    # PS:进而利用two sum解法，利用hashmap把二维降为一维
    def countTriplets2(self, arr):
        preXOR = [0]
        for a in arr:
            preXOR.append(preXOR[-1] ^ a)
        res = 0
        for i in range(len(arr)):
            for k in range(i + 1, len(arr)):
                if preXOR[k + 1] == preXOR[i]:
                    res += k - i
        return res

    # preSum
    def countTriplets(self, arr):
        preXOR = [0]
        for a in arr:
            preXOR.append(preXOR[-1] ^ a)
        res = 0
        for i in range(len(arr) + 1):
            for j in range(i + 1, len(arr) + 1):
                for k in range(j + 1, len(arr) + 1):
                    xor1 = preXOR[j] ^ preXOR[i]
                    xor2 = preXOR[k] ^ preXOR[j]
                    if xor1 == xor2:
                        res += 1
        return res

test = Solution()
print test.countTriplets2([2,3,1,6,7])
print test.countTriplets2([1,1,1,1,1])
print test.countTriplets2([2,3])
print test.countTriplets2([1,3,5,7,9])
print test.countTriplets2([7,11,12,9,5,2,7,17,22])