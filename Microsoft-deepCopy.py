# -*- coding: utf-8 -*-
# KV class类似hashmap结构，value是另一个hashmap，利用get set进行递归deep copy
# KV => String : KV()
class KV(object):
    def __init__(self):
        return
    def listKeys(self):
        return
    def getValue(self, key):
        return
    def setKeyValue(self, key, value):
        return

def deepCopy(source):

    def helper(source):
        if source is None:
            return None

        curr = KV()
        for k in source.listKeys():
            value = helper(source.getValue(k))
            curr.setKeyValue(k, value)

        return curr

    return helper(source)

source = KV()
copySource = deepCopy(source)