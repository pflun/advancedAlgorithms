# -*- coding: utf-8 -*-
class Solution(object):
    # def deserialize(self, data):
    #     vals = iter(data)
    #
    #     root = self.helper(vals)
    #     return root
    #
    # def helper(self, vals):
    #     val = next(vals)
    #     print val
    #     self.helper(vals)
    def test(self, nums):
        row = [0] * len(nums)
        res = []
        for i in range(len(nums)):
            # shallow copy 浅拷贝，否则res赋值会改变row（也会改变其他行in matrix）
            res.append(row[:])
        res[0][0] = 1
        return res

    def test2(self, nums):
        return type(25)

    def test3(self, nums):
        del nums[3:6]
        for num in nums:
            print nums.index(num)
        return nums

    def test4(self, nums):
        for num in nums:
            print num
            if num == 4:
                del nums[2:5]
                break
        students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
        newStudents = sorted(students, key=lambda x: x[2])

        return newStudents

    def test5(self, nums):
        print nums[:3], nums[3:]

        # nums = filter(lambda x: x % 2 == 0, nums)
        nums = reduce(lambda x, y: x * y, nums)
        return nums

    def test6(self, nums):
        nums = ''.join(nums)
        print nums
        # for x in range(ord('a'), ord('z') + 1):
        #     print chr(x)

    def test7(self, nums):
        for k in range(len(nums) - 1, 1, -1):
            print k

    def test8(self, nums):
        import heapq
        heap = nums[:2]
        heapq.heapify(heap)
        # difference heapreplace and heappushpop
        for num in nums[2:]:
            print heapq.heapreplace(heap, num)
            # print heapq.heappushpop(heap, num)

    def test9(self, nums):
        # sort decending
        # in-place
        nums.sort(reverse=True)
        # Or nums = sorted(nums, reverse=True)
        for i in range(0, 1):
            print nums[i]
        print int('021')
        print nums[:1]
        print [8] + nums
        return nums

test = Solution()
print test.test9([11, 15, 2, 7, 6, 3])

