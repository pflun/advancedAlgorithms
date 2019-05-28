class Solution(object):
    def lengthLongestPath(self, input):
        if len(input) == 0:
            return []

        stack = []
        res = []
        pre = -1
        input = input.split('\n')
        for str in input:
            # get current level by count how many \t
            level = str.count('\t')
            # remove \t or \t\t ...
            str = str.replace("\t", "")

            # if at next level
            if pre < level:
                stack.append(str)
            # if at same level
            elif pre == level:
                stack.pop()
                stack.append(str)
            # if prev is end of curr_dir (curr is a new dir)
            elif pre > level:
                for k in range(pre - level + 1):
                    stack.pop()
                stack.append(str)

            # if found file, add stack element together append to res
            if '.' in str:
                tmp = stack[0]
                for i in stack[1:]:
                    tmp = tmp + '/' + i
                res.append(tmp)

            # curr_level become pre_level in next for loop
            pre = level

        return res

test = Solution()
print test.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")