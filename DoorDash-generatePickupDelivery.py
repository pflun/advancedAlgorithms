class Solution(object):
    # O(n!)
    def generatePickupDelivery(self, n):
        self.res = []
        pickup = ['P' + str(idx) for idx in range(1, n + 1)]
        delivery = ['D' + str(idx) for idx in range(1, n + 1)]

        def dfs(pickup, delivery, tmp, picked, delivered):
            if len(tmp) == 2 * len(pickup):
                self.res.append(tmp[:])
                return
            for i in range(len(pickup)):
                if i not in picked:
                    tmp.append(pickup[i])
                    picked.add(i)
                    dfs(pickup, delivery, tmp, picked, delivered)
                    tmp.pop()
                    picked.remove(i)

            for i in range(len(delivery)):
                if i in picked and i not in delivered:
                    tmp.append(delivery[i])
                    delivered.add(i)
                    dfs(pickup, delivery, tmp, picked, delivered)
                    tmp.pop()
                    delivered.remove(i)

        dfs(pickup, delivery, [], set(), set())

        return self.res

test = Solution()
print test.generatePickupDelivery(3)
print test.generatePickupDelivery(1)

class IsValidSolution(object):
    def isValidPickupDelivery(self, arr):
        dic = {}
        for a in arr:
            if a[0] == 'P':
                if a in dic:
                    return False
                else:
                    dic[a] = 0
            elif a[0] == 'D':
                p = 'P' + a[1:]
                if p not in dic:
                    return False
                # P1 D1 D1
                elif dic[p] > 0:
                    return False
                elif dic[p] == 0:
                    dic[p] = 1
        # only P1 but no D1 appear
        for v in dic.values():
            if v != 1:
                return False
        return True

test2 = IsValidSolution()
print test2.isValidPickupDelivery(['P3', 'P3', 'P1', 'D1', 'P2', 'D2'])
print test2.isValidPickupDelivery(['P3', 'D3', 'D1', 'P1', 'P2', 'D2'])
print test2.isValidPickupDelivery(['P3', 'D3', 'P1', 'D1', 'P2', 'D2', 'P1'])
print test2.isValidPickupDelivery(['P3', 'D3', 'P1', 'D1', 'P2', 'D2', 'D1'])
print test2.isValidPickupDelivery(['P3'])
# for t in test.generatePickupDelivery(3):
#     print test2.isValidPickupDelivery(t)
