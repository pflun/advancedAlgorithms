# -*- coding: utf-8 -*-
# 单笔 transaction 金额 > $2000，直接算 fraud
# 同一个 account 在 60 分钟内，如果在不同 location 发生 transaction，也算 fraud

class Solution(object):
    def findFraudTransactions(self, transactions):
        # 1. 拆解 transaction 并且记录它的原始形式（因为要原样返回）
        parsed_txs = []
        for orig_tx in transactions:
            parts = orig_tx.split(',')
            name = parts[0]
            amount = int(parts[1])
            location = parts[2]
            time = int(parts[3])
            parsed_txs.append((name, amount, location, time, orig_tx))
            
        # 2. 按照 account_name 分组 (历史记录)，同时按时间排序
        # 这样可以方便处理 rule 2 (60 分钟内异地)
        history = {}  # name -> list of (time, location, orig_tx)
        for tx in parsed_txs:
            name, amount, location, time, orig_tx = tx
            if name not in history:
                history[name] = []
            history[name].append((time, location, orig_tx))
            
        for name in history:
            history[name].sort()  # 按时间排序

        # 3. 检查每个 transaction 是否满足 fraud 规则
        fraud_set = set()  # 使用 set 去重，防止同一个 tx 被多个规则重复判断为 fraud
        
        for i in range(len(parsed_txs)):
            name, amount, location, time, orig_tx = parsed_txs[i]
            
            # Rule 1: 单笔金额 > 2000
            if amount > 2000:
                fraud_set.add(orig_tx)
                
            # Rule 2: 60分钟内同人异地
            # 我们去查找这个人在这个时候之前的所有记录
            # 因为数据已经按照时间排序了，从后往前找最快
            # （也可以用 Sliding Window 双指针，这里简单处理，由于按人分组，每个人的数据量通常不大）
            user_history = history[name]
            
            # 找到当前 tx 在 user_history 中的 idx
            # 这里偷个懒，因为我们是在遍历所有的 tx，我们可以直接用双重循环或者二分查找
            # 为了“简单易懂”，我们直接遍历 user_history
            for prev_time, prev_location, prev_tx in user_history:
                # 只需要检查时间比当前时间早，并且时间差 <= 60 分钟的
                if time >= prev_time and time - prev_time <= 60:
                    # 如果地点不同，说明构成了 60分钟内异地，两个 tx 都是 fraud
                    if location != prev_location:
                        fraud_set.add(orig_tx)
                        fraud_set.add(prev_tx)
                        # 注意：不要 break，因为可能之前的多笔都被判定为 fraud

        return list(fraud_set)


# 测试代码
if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1: Rule 1 (单笔 > 2000)
    tx1 = ["alice,2001,newyork,10", "bob,100,seattle,20"]
    print "Test 1:", sol.findFraudTransactions(tx1)  # ['alice,2001,newyork,10']
    
    # 测试用例 2: Rule 2 (60 分钟内异地)
    tx2 = ["alice,100,newyork,10", "alice,200,boston,65"]  
    # 65-10 = 55 <= 60, 两笔都是 fraud
    print "Test 2:", sol.findFraudTransactions(tx2)
    
    # 测试用例 3: 边界情况，时间刚好 60 分钟
    tx3 = ["alice,100,newyork,10", "alice,200,boston,70"]
    print "Test 3:", sol.findFraudTransactions(tx3) 
    
    # 测试用例 4: 超过 60 分钟，不是 fraud
    tx4 = ["alice,100,newyork,10", "alice,200,boston,80"]
    print "Test 4:", sol.findFraudTransactions(tx4)