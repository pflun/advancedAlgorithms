# -*- coding: utf-8 -*-
# void addStocksVolume(string stockSymbol, int volume)
# vector<string> topKstocks(int k)
#
# addStocksVolume receives a symbol (INTC, APPL, etc) plus a volume which you cumulate over time.
# topKstocks would return the k stocks with the highest volume.
# 有个执行交易的interface：
# execute_trade(ticker, quantity)
# 被调用很多次
# 问：打印出当天交易量top k tickers

import heapq
class Solution(object):
    def __init__(self):
        self.stocks = {}

    def addStocksVolume(self, stockSymbol, volume):
        self.stocks[stockSymbol] = self.stocks.get(stockSymbol, 0) + volume

    # max heap as pop the most volume
    def topKstocks(self, k):
        heap = []
        heapq.heapify(heap)
        for symbol, volume in self.stocks.items():
            heapq.heappush(heap, [-volume, symbol])
        res = []
        while k > 0:
            k -= 1
            curr = heapq.heappop(heap)
            res.append(curr[1])
        return res

    # min heap as ditch less volume
    def topKstocks2(self, k):
        heap = []
        heapq.heapify(heap)
        for symbol, volume in self.stocks.items():
            if len(heap) < k:
                heapq.heappush(heap, [volume, symbol])
            else:
                heapq.heappush(heap, [volume, symbol])
                heapq.heappop(heap)
        return [x[1] for x in heap]

test = Solution()
test.addStocksVolume('AAPL', 1)
test.addStocksVolume('AAPL', 2)
test.addStocksVolume('MSFT', 2)
test.addStocksVolume('NVDA', 4)
test.addStocksVolume('GOOG', 5)
print test.topKstocks(3)