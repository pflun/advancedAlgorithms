# -*- coding:utf-8 -*-


class HashTable:
    def __init__(self, size):
        self.elem = [None for i in range(size)]  # 使用list数据结构作为哈希表元素保存方法
        self.count = size  # 最大表长

    def hash(self, key):
        return key % self.count  # 散列函数采用除留余数法

    def insert_hash(self, key):
        # print key
        """插入关键字到哈希表内"""
        address = self.hash(key)  # 求散列地址
        # print address
        while self.elem[address] != None:  # 当前位置已经有数据了，发生冲突。
            address = (address + 1) % self.count  # 线性探测下一地址是否可用
        # print address
        self.elem[address] = key  # 没有冲突则直接保存。
        print self.elem

    def search_hash(self, key):
        """查找关键字，返回布尔值"""
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address + 1) % self.count
            if not self.elem[address] or address == star:  # 说明没找到或者循环到了开始的位置
                return False
        return True


if __name__ == '__main__':
    list_a = [0, 12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    hash_table = HashTable(len(list_a))
    for i in list_a:
        hash_table.insert_hash(i)

    for i in hash_table.elem:
        if i:
            print((i, hash_table.elem.index(i)))
    print(hash_table.search_hash(15))
    print(hash_table.search_hash(33))