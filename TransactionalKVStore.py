# -*- coding: utf-8 -*-
class TransactionalKVStore(object):
    def __init__(self):
        # 字典栈：栈底是全局数据，栈顶是当前最新事务的数据
        # 初始状态下，栈里只有一个空字典，代表全局状态
        self.kv_stack = [{}]
        
        # 计数栈：用于 O(1) 时间复杂度实现 count(value)
        # 结构与 kv_stack 保持同步
        self.count_stack = [{}]

    def set(self, key, value):
        current_kv = self.kv_stack[-1]
        current_counts = self.count_stack[-1]

        # 1. 处理旧值：如果这个 key 之前有值，我们需要把旧值的计数减 1
        # 注意：这里必须调用 self.get(key) 去全局查找旧值，而不能只看当前事务
        old_value = self.get(key)
        if old_value is not None:
            # 在当前事务的计数栈中，将旧值的数量减 1
            # 如果当前事务还没有记录这个旧值的数量，就先去全局查一下它的数量
            current_counts[old_value] = current_counts.get(old_value, self.count(old_value)) - 1

        # 2. 设置新值：只写在当前事务的字典里，绝不修改底层数据
        current_kv[key] = value

        # 3. 处理新值：将新值的计数加 1
        current_counts[value] = current_counts.get(value, self.count(value)) + 1

    def get(self, key):
        # 从栈顶（最新事务）开始，一层层往下找，直到找到全局状态
        for i in range(len(self.kv_stack) - 1, -1, -1):
            if key in self.kv_stack[i]:
                val = self.kv_stack[i][key]
                # 墓碑机制 (Tombstone)：
                # 如果读到 False，说明这个 key 在某个事务中被删除了。
                # 此时必须立刻停止往下找，并返回 None 表示不存在。
                return val if val is not False else None
        return None

    def delete(self, key):
        # 删除操作本质上也是一种“修改”
        old_value = self.get(key)
        if old_value is not None:
            # 1. 把旧值的计数减 1
            current_counts = self.count_stack[-1]
            current_counts[old_value] = current_counts.get(old_value, self.count(old_value)) - 1
            
            # 2. 放置墓碑：在当前事务中把值设为 False
            # 这样下一次 get() 往下找的时候，看到 False 就知道它被删了
            self.kv_stack[-1][key] = False

    def count(self, value):
        # 和 get 的逻辑一样，从栈顶往下找这个 value 的最新计数
        for i in range(len(self.count_stack) - 1, -1, -1):
            if value in self.count_stack[i]:
                return self.count_stack[i][value]
        return 0

    def begin(self):
        # 开启新事务：只需要往栈顶推入两个空字典即可，O(1) 操作
        self.kv_stack.append({})
        self.count_stack.append({})

    def rollback(self):
        # 回滚事务：如果栈里只有一个字典，说明没有开启事务，报错
        if len(self.kv_stack) == 1:
            raise Exception("No active transaction to rollback")
            
        # 直接把栈顶的字典扔掉，当前事务的所有修改瞬间灰飞烟灭，O(1) 操作
        self.kv_stack.pop()
        self.count_stack.pop()

    def commit(self):
        if len(self.kv_stack) == 1:
            raise Exception("No active transaction to commit")
            
        # 1. 把当前事务的字典弹出来
        local_kv = self.kv_stack.pop()
        local_counts = self.count_stack.pop()
        
        # 2. 把当前事务的修改，合并到它下面那一层的字典里
        # 如果下面那一层是全局状态，这就相当于落盘了
        self.kv_stack[-1].update(local_kv) # A_dict.update(B_dict) is merge
        self.count_stack[-1].update(local_counts)


# ==========================================
# 测试代码
# ==========================================
if __name__ == "__main__":
    db = TransactionalKVStore()
    
    # 全局操作
    db.set("A", "foo")
    db.set("B", "foo")
    print "Count of 'foo':", db.count("foo") # 期待: 2

    # 开启事务 1
    db.begin()
    db.set("A", "bar")
    print "Count of 'foo' after A->bar:", db.count("foo") # 期待: 1
    print "Get A:", db.get("A")     # 期待: "bar"

    # 回滚事务 1
    db.rollback()
    print "Get A after rollback:", db.get("A")     # 期待: "foo"
    print "Count of 'foo' after rollback:", db.count("foo") # 期待: 2
    
    # 开启事务 2 测试删除
    db.begin()
    db.delete("A")
    print "Get A after delete:", db.get("A") # 期待: None
    print "Count of 'foo' after delete A:", db.count("foo") # 期待: 1
    
    # 提交事务 2
    db.commit()
    print "Get A after commit:", db.get("A") # 期待: None
    print "Count of 'foo' after commit:", db.count("foo") # 期待: 1
