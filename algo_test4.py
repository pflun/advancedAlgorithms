class Solution(object):
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0 or s < 0:
            return None

        counter = nums[0]
        size = float('inf')
        left = 0
        right = 0

        while right < len(nums) and left < len(nums) - 1:
            print left, right, counter, size
            if counter < s:
                right += 1
                counter += nums[right]
            else:
                size = min(size, right - left + 1)
                counter -= nums[left]
                left += 1

        return size

    def minSubArrayLen2(self, s, nums):
        size = float('inf')
        j = 0
        counter = 0

        for i in range(len(nums)):
            while j < len(nums) - 1 and counter < s:
                j += 1
                counter += nums[j]
            if counter >= s:
                size = min(size, j - i)
            counter -= nums[i]

        if size == float('inf'):
            return 0
        return size

test = Solution()
print test.minSubArrayLen2(11, [1,2,3,4,5])


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

    def isValidBST(self, root):

        def inorder(root, res):
            if not root:
                return None

            if root.left:
                inorder(root.left, res)

            res.append(root.val)

            if root.right:
                inorder(root.right, res)

            return res

        return inorder(root, [])

    def test1(self, nums):
        operator = '+'
        print eval('-2' + operator + '3')
        print [0 for _ in range(len(nums))]
        return nums[:5], nums[6:]

test = Solution1()
print test.isValidBST(test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print test.test1([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 11])