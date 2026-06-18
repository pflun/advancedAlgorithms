# -*- coding: utf-8 -*-

class Solution(object):
    def movesToStamp(self, stamp, target):
        s_len, t_len = len(stamp), len(target)
        # 字符串不可变，转成 list 方便我们在原地把字母修改成 '?'
        target_list = list(target) 
        res = []
        stars = 0 # 记录目前有多少个字母已经被变成了 '?'
        
        # 辅助函数 1：检查在 target 的索引 i 处，能不能“撕邮票”
        def can_unstamp(i):
            has_letter = False # 必须至少包含一个真实的字母，如果全是 '?' 就没必要撕了
            for j in range(s_len):
                if target_list[i + j] == '?':
                    continue # '?' 是百搭符，代表这里曾经被盖过章，直接跳过
                if target_list[i + j] != stamp[j]:
                    return False # 只要有一个真实字母不匹配，就不能在这里撕
                has_letter = True
            return has_letter
            
        # 辅助函数 2：执行“撕邮票”操作，把匹配的字母变成 '?'
        def do_unstamp(i):
            count = 0
            for j in range(s_len):
                if target_list[i + j] != '?':
                    target_list[i + j] = '?'
                    count += 1 # 记录这次新撕掉了几个字母
            return count

        # 主循环：只要还没全部变成 '?'，就继续尝试撕
        while stars < t_len:
            changed = False # 标记这一轮遍历有没有成功撕掉任何邮票
            
            # 尝试每一个可能的起始位置 (从 0 到 t_len - s_len)
            for i in range(t_len - s_len + 1):
                if can_unstamp(i):
                    stars += do_unstamp(i) # 执行撕邮票，并更新 '?' 的总数
                    res.append(i)          # 记录这次撕邮票的位置
                    changed = True         # 标记本轮有进展
            
            # 如果完整遍历了一圈，一张邮票都没撕下来，说明卡死了，无解
            if not changed:
                return []
                
        # 因为我们是“倒着撕”的，所以正向盖章的顺序需要把结果反转
        return res[::-1]

# ==========================================
# 测试代码
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    print sol.movesToStamp("abc", "ababc") # 期待输出: [0, 2]
    print sol.movesToStamp("abca", "aabcaca") # 期待输出: [3, 0, 1]
