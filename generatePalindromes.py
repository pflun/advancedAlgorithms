# -*- coding: utf-8 -*-
# permute前半段 ＋ 中间奇数个 ＋ 复制前半段
class Solution(object):
    def generatePalindromes(self, s):
        dic = {}
        counter = 0
        mid = []
        permute = []
        res = []

        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for key, val in dic.items():
            if val % 2 != 0:
                # 生成中间奇数数组
                mid = [key] * val
                counter += 1
                # 一组以上奇数则不成立
                if counter > 1:
                    return []
            else:
                # 所有偶数个元素除以2，扔进permute里，复制前半段时会补回来
                for _ in range(val / 2):
                    permute.append(key)

        # permute start
        self.permute = []
        self.used = [False] * len(permute)

        def dfs(permute, tmp):
            if len(tmp) == len(permute):
                # shallow copy
                self.permute.append(tmp[:])

            for i in range(len(permute)):
                if self.used[i]:
                    continue
                # [1, 2] are used
                self.used[i] = True
                tmp.append(permute[i])
                dfs(permute, tmp)
                # backtracking:
                # after dfs([1, 2]) done, set used[2] to False for for loop [1, 3] && 2 not used yet
                self.used[i] = False
                tmp.pop()

        dfs(permute, [])

        # 最终结果是由 前半部分 ＋ 中间奇数 ＋ 反转前半部分 获得
        for arr in self.permute:
            first = arr
            # Tip: reverse list
            second = arr[::-1]
            res.append(''.join(first + mid + second))

        return res


test = Solution()
print test.generatePalindromes("ccareeercac")
# print test.generatePalindromes("aabb")