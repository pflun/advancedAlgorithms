# -*- coding: utf-8 -*-
# Reverse Linked List template
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        # 双指针法 (Two Pointers)
        prev = None      # 初始时，前一个节点是空
        curr = head      # 当前节点从头开始

        while curr:
            # 1. 备份：保存下一个节点，不然等下线断了就找不到了
            next_temp = curr.next 
            
            # 2. 反转：把当前节点的箭头，指向上一个节点
            curr.next = prev 
            
            # 3. 移动：两个指针整体往右平移一步，准备处理下一个节点
            prev = curr
            curr = next_temp
            
        # 循环结束时，curr 变成了 None，prev 刚好停在原链表的最后一个节点（也就是新链表的头）
        return prev
