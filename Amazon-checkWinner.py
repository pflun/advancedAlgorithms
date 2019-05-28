# -*- coding: utf-8 -*-
# codeList之间允许插入不同水果，其他的双指针
class Solution(object):
    def checkWinner(self, codeList, shoppingCart):
        if len(codeList) == 0:
            return 1
        if len(shoppingCart) == 0:
            return 0

        pCart = 0

        for fruits in codeList:
            i = 0
            if fruits[i] != shoppingCart[pCart]:
                pCart = self.findNext(fruits[i], pCart, shoppingCart)

            while i < len(fruits):
                if fruits[i] == shoppingCart[pCart]:
                    i += 1
                    pCart += 1
                elif fruits[i] == "anything":
                    i += 1
                    pCart += 1
                else:
                    return 0
        return 1

    def findNext(self, fruit, curr, shoppingCart):
        while fruit != shoppingCart[curr]:
            curr += 1
        return curr



test1 = Solution()
print test1.checkWinner([["apple", "apple"], ["banana", "anything", "banana"]], ["orange", "apple", "apple", "banana", "orange", "banana"] )