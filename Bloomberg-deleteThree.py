# -*- coding: utf-8 -*-
# http://www.1point3acres.com/bbs/thread-302316-1-1.html
# 一维消消乐
class Solution(object):
    # need debug
    def deleteThree(self, string):

        stack1 = [string[0]]
        stack2 = [1]
        i = 1
        while i < len(string):
            if string[i] == stack1[-1]:
                stack1.append(string[i])
                stack2[-1] += 1
            else:
                if stack2[-1] >= 3:
                    val = stack2.pop()
                    stack1 = stack1[:len(stack1) - val]
                    if string[i] != stack1[-1]:
                        stack2.append(1)
                        stack1.append(string[i])
                    # else:
                        # Need debug
                else:
                    stack2.append(1)
                    stack1.append(string[i])
            i += 1

        return str(stack1)

class Solution2(object):
    def deleteThree(self, string):
        arr = list(string)
        # Add and pop '#' to deal with '122211' -> '111' (need diff elem to del arr)
        arr.append('#')
        self.res = ''

        def helper(arr):
            if len(arr) < 3:
                self.res = arr
            counter = 1
            flag = True

            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1]:
                    counter += 1
                else:
                    if counter >= 3:
                        del arr[i - counter:i]
                        flag = False
                        break
                    counter = 1

            if flag:
                self.res = arr
            else:
                helper(arr)

        helper(arr)

        self.res.pop()
        return ''.join(self.res)


test = Solution2()
print test.deleteThree('115223333211')


