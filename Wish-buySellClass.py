# -*- coding: utf-8 -*-
# 设计一个 买/卖一个商品的class,提供两个功能,buy(p rice, quantity)和sell(price, quantity),意思就是有人出多少钱买多少个这个商
# 品,或者有人标价多少钱卖这个商品,返回值是买到或者卖出的数量,例子:
# sell(10, 20) 返回0,暂时没人买,把这个数据存着
# buy(5, 20) 返回0,没有人用<=5的价格卖这个商品,把这个订单也存起来
# sell(4, 25) 返回20,上一行那个买家就买到了20个,然后剩5个存起来
# buy(12, 30) 返回25,第一行的20个被买了,还有上一行剩的5个也被买了,然后还差5个的订单,存起来
# 另外,
# 如果有多个卖家用不同的价格卖同一个商品,并且价格都低于当前buy的价格,先买哪个无所谓。反之亦然
# bug
class buySellClass(object):
    def __init__(self):
        self.sells = {}
        self.buys = {}

    def sell(self, price, quantity):
        if len(self.buys) == 0:
            if quantity != 0:
                if price in self.sells:
                    self.sells[price] += quantity
                else:
                    self.sells[price] = quantity
            return 0
        res = 0
        for k in sorted(self.buys.keys()):
            if quantity == 0:
                break
            v = self.buys[k]
            if k <= price:
                if quantity >= v:
                    quantity -= v
                    res += v
                    self.buys.pop(k)
                else:
                    v -= quantity
                    res += quantity
                    self.buys[k] = v
            else:
                if quantity != 0:
                    if price in self.sells:
                        self.sells[price] += quantity
                    else:
                        self.sells[price] = quantity
                break
        return res

    def buy(self, price, quantity):
        if len(self.sells) == 0:
            if quantity != 0:
                if price in self.buys:
                    self.buys[price] += quantity
                else:
                    self.buys[price] = quantity
            return 0
        res = 0
        for k in sorted(self.sells.keys(), reverse=True):
            if quantity == 0:
                break
            v = self.sells[k]
            if k >= price:
                if quantity >= v:
                    quantity -= v
                    res += v
                    self.sells.pop(k)
                else:
                    v -= quantity
                    res += quantity
                    self.sells[k] = v
            else:
                if quantity != 0:
                    if price in self.buys:
                        self.buys[price] += quantity
                    else:
                        self.buys[price] = quantity
                break
        return res

test = buySellClass()
print test.sell(10, 20)
print test.buy(5, 20)
print test.sell(4, 25)
print test.buy(12, 30)