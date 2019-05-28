import heapq

import math
import random
from cStringIO import StringIO

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)  # create a min-heap whose size is k
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
            # or use:
            # heapq.heappushpop(heap, num)
        print heap
        return heap[0]

    # Show heap structure
    def show_tree(self, tree, total_width=36, fill=' '):
        output = StringIO()
        last_row = -1
        for i, n in enumerate(tree):
            if i:
                row = int(math.floor(math.log(i + 1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2 ** row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print output.getvalue()
        print '-' * total_width
        print
        return

test = Solution()
print test.findKthLargest([3,2,1,5,6,4], 6)

# Test sample
# data = random.sample(range(1,8), 7)
# print 'data: ', data
# test.show_tree(data)