# https://www.hack2hire.com/companies/robinhood/coding-questions/67d739167e869a20cd523ea8/practice?questionId=67d793931989183df53824a0&src=eg1
# You have a list of orders and an initial inventory of stock fractions, both sorted by stock symbol. Each order is given
# as a list in the format [<symbol>, <order_type>, <quantity>, <unit_price>]
# Buy orders:
# If the current inventory holds enough fractional shares to cover the buy order, simply subtract the order amount from the inventory.
# If not, determine the shortfall and purchase enough whole shares to cover it. After the purchase, subtract the order amount and keep any leftover as the new fractional inventory.
# Sell orders:
# Add the sold fraction to the inventory, then adjust the total by removing any whole shares, keeping only the fractional part to ensure the inventory remains less than one whole share.
class Solution:
    def fractionInvent(self, orders, inventory):
        res = []
        dic = {}
        for stock in inventory:
            dic[stock[0]] = int(stock[1])
        for o in orders:
            symbol = o[0]
            order_type = o[1]
            unit_price = int(o[3])
            quantity = int(o[2][1:]) * 100 / unit_price if o[2][0] == '$' else int(o[2])
            if order_type == 'B':
                if dic[symbol] >= quantity:
                    dic[symbol] -= quantity
                else:
                    quantity = quantity % 100
                    dic[symbol] = dic[symbol] - quantity if dic[symbol] >= quantity else dic[symbol] + 100 - quantity
            elif order_type == 'S':
                dic[symbol] = (dic[symbol] + quantity) % 100
        for k, v in dic.items():
            res.append([k, v])
        return res

test = Solution()
print test.fractionInvent([["AAPL", "B", "42", "100"], ["GOOG", "S", "$80", "160"]], [["AAPL", "99"], ["GOOG", "60"]])
print test.fractionInvent([["AAPL","B","$42","100"]], [["AAPL","50"]])
print test.fractionInvent([["AAPL","S","75","100"]], [["AAPL","60"]])
