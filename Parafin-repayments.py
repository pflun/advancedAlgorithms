# -*- coding: utf-8 -*-
# Businesses pay back advances using a percentage of their sales. Some businesses pay back based on their daily sales, while others pay back on a weekly basis.
# Businesses can switch their payment cadence once a day and changes take effect from next day onwards. You will be provided with sales data for each day during the period.
# Given a set of businesses, their payment cadence history and their daily sales, compute the repayments that we expect from the businesses.
# example input
# [{
#     "name": "Da Sichuan",
#     "repayment_rate": 10.0,
#     "payment_cadence": {
#         2: "weekly",
#         5: "daily",
#     },
#     "sales": {
#         1: 500.0,
#         2: 300.0,
#         3: 400.0,
#         4: 550.0,
#         5: 200.0,
#         6: 350.0,
#     }
# }]
# example output:
# [{
#     "name": "Da Sichuan",
#     "repayments": {
#         1: 50.0,
#         2: 30.0,
#         5: 115.0,
#         6: 35.0,
#     }
# }]

class Solution(object):
    def computeRepayments(self, businesses):
        res = []
        for b in businesses:
            name = b.get("name")
            # 注意: rate 转成小数
            rate = b.get("repayment_rate", 0.0) / 100.0
            cadenceHistory = b.get("payment_cadence", {})
            sales = b.get("sales", {})
            
            if not sales and not cadenceHistory:
                res.append({"name": name, "repayments": {}})
                continue
                
            # 获取所有出现的日子，用来确定遍历的开始和结束
            # Python 2.7 中 .keys() 返回 list，可以直接相加
            allDays = sales.keys() + cadenceHistory.keys()
            minDay = min(allDays)
            maxDay = max(allDays)
            
            repayments = {}
            currentCadence = "daily"
            weeklyAcc = 0.0
            weeklyDaysCount = 0
            
            # 遍历完整的连续自然天，包括 missing days
            for day in range(minDay, maxDay + 1):
                # 1. 检查昨天 (day - 1) 是否有更改申请，如果有，今天就生效新的 cadence
                if (day - 1) in cadenceHistory:
                    newCadence = cadenceHistory[day - 1]
                    if currentCadence != newCadence:
                        currentCadence = newCadence
                        weeklyDaysCount = 0 # 切换 cadence 后重置天数计数器
                        
                # 2. 计算当天的抽水
                dailySale = sales.get(day, 0.0)
                dailyRepayment = dailySale * rate
                
                # 3. 根据当前的 cadence 决定是立即 payout 还是累加
                if currentCadence == "daily":
                    if dailyRepayment > 0:
                        repayments[day] = dailyRepayment
                        
                elif currentCadence == "weekly":
                    weeklyAcc += dailyRepayment
                    weeklyDaysCount += 1
                    
                    # 检查今天是否必须把 weeklyAcc 清算 payout 掉
                    payoutTriggered = False
                    
                    # 条件a: 刚好凑满了 7 天
                    if weeklyDaysCount == 7:
                        payoutTriggered = True
                    # 条件b: 今天发起了切换回 "daily" 的请求 (明天就失效了，所以今天必须清算)
                    elif day in cadenceHistory and cadenceHistory[day] == "daily":
                        payoutTriggered = True
                    # 条件c: 已经是数据的最后一天了，收尾清算
                    elif day == maxDay:
                        payoutTriggered = True
                        
                    if payoutTriggered:
                        if weeklyAcc > 0:
                            repayments[day] = weeklyAcc
                        # 清空累加池，重置天数
                        weeklyAcc = 0.0
                        weeklyDaysCount = 0
            
            res.append({
                "name": name,
                "repayments": repayments
            })
            
        return res

if __name__ == "__main__":
    example_input = [{
        "name": "Da Sichuan",
        "repayment_rate": 10.0,
        "payment_cadence": {
            2: "weekly",
            5: "daily",
        },
        "sales": {
            1: 500.0,
            2: 300.0,
            3: 400.0,
            4: 550.0,
            5: 200.0,
            6: 350.0,
        }
    }]
    
    test = Solution()
    output = test.computeRepayments(example_input)
    import json
    print json.dumps(output, indent=4)
