class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        if len(A) < 1:
            return 0
        elif len(A) == 1:
            return A.pop()
        buff = A
        counter = 0
        for i in A:
            for j in buff:
                if i == j:
                    counter +=1
                    if counter == 2:
                        A.remove(i)
                        A.remove(i)
                        counter = 0
                else:
                    continue
        B = A.pop()
        return B

    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            print num , dic[num]
        print dic
        for key, val in dic.items():
            if val == 1:
                return key

test = Solution()
# print test.singleNumber1([1,1,2,2,4,4,5,6,7,6,7,100,-1,-2,-1,100,3,-2,3])
test.singleNumber1([5,1,2,1,2,4,4,5,6,7,6])