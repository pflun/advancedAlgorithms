class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        if n == 1:
            return 11
        init = 11
        tmp_list = []
        dic = {}
        for i in range(n-1):
            print "init: ", init
            tmp_num = [int(x) for x in str(init)]
            for num in tmp_num:
                dic[num] = dic.get(num, 0) + 1
            print dic.items()

            for key, val in dic.items():
                tmp_list += [val, key]
                print tmp_list
                tmp_list = map(str, tmp_list)
                tmp_list = ''.join(tmp_list)
                init = int(tmp_list)
                print init
            dic = {}

            # return tmp_num

# Idea here is keep track of the first letter in the sequence and count consecutive occurances. Once you encounter a new letter you add the previous count and letter to the chain. Repeat n-1 times (since we seeded the initial '1' case). We always update temp after the inner loop since we will never have already added the last sequence.

    def countAndSay2(self, n):
        s = '1'
        for _ in range(n - 1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index - 1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index - 1])
                    count = 1

            # execute last step for s[index] == s[index - 1], append count and value
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s

test = Solution()
print test.countAndSay2(5)