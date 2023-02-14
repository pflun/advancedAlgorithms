class Solution(object):
    def invalidTransactions(self, transactions):
        # {50: {'alice': ['beijing']}
        dic = {}
        res = []
        for transaction in transactions:
            t = transaction.split(',')
            name = t[0]
            time = int(t[1])
            amount = int(t[2])
            city = t[3]
            if time not in dic:
                dic[time] = {name : [city]}
            else:
                if name not in dic[time]:
                    dic[time][name]=[city]
                else:
                    dic[time][name].append(city)

        for transaction in transactions:
            t = transaction.split(',')
            name = t[0]
            time = int(t[1])
            amount = int(t[2])
            city = t[3]
            if amount > 1000:
                res.append(transaction)
                continue
            # check adjacent 120 minutes
            for j in range(time - 60, time + 61):
                if j not in dic:
                    continue
                if name not in dic[j]:
                    continue
                # same name in different cities
                for c in dic[j][name]:
                    if c != city:
                        res.append(transaction)
                        break
                # if len(dic[j][name]) > 1 or dic[j][name][0] != city:
                #     res.append(transaction)
                #     break
        return res


test = Solution()
print test.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"])
print test.invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"])
print test.invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"])