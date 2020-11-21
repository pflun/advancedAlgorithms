# -*- coding: utf-8 -*-
# [{}, {}] 用下一层map覆盖以前的map，这样get时从后往前先get到就return
# commit就用当前层覆盖上一层map，支持multiple transaction，这样上一个transaction里commit的kv在下一次commit时覆写掉
from typing import *

class KVStore:
    def __init__(self):
        self.stack = [{}]

    def set(self, key, value):
        """O(1)"""
        self.stack[-1][key] = value

    def get(self, key):
        """O(transaction)"""
        for i in range(len(self.stack) - 1, -1, -1):
            if key in self.stack[i]:
                return self.stack[i][key]

    def begin(self):
        """O(1)"""
        self.stack.append({})

    def commit(self):
        """O(n_keys)"""
        last_dic = self.stack.pop()

        for k, v in last_dic.items():
            self.stack[-1][k] = v

    def rollback(self):
        """O(1)"""
        self.stack.pop()


def test_KVStore():
    kv = KVStore()
    kv.set(1, 3)

    assert kv.get(1) == 3
    assert kv.get(2) is None


def test_KVStore_single_transaction():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)
    assert kv.get(1) == 3
    assert kv.get(2) == 4
    kv.commit()

    assert kv.get(1) == 3
    assert kv.get(2) == 4


def test_KVStore_rollback():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)
    assert kv.get(1) == 3
    assert kv.get(2) == 4
    kv.rollback()

    assert kv.get(1) == 3
    assert kv.get(2) is None


def test_KVStore_multiple_begin():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)

    kv.begin()
    kv.set(3, 5)

    assert kv.get(1) == 3
    assert kv.get(2) == 4
    assert kv.get(3) == 5

    kv.commit()

    assert kv.get(1) == 3
    assert kv.get(2) == 4
    assert kv.get(3) == 5

    kv.rollback()

    assert kv.get(1) == 3
    assert kv.get(2) == None
    assert kv.get(3) == None