class Solution(object):
    def displayTable(self, orders):
        tables = {}
        foods = set()
        # tid => {food name => count}
        for o in orders:
            tid = int(o[1])
            food = o[2]
            foods.add(food)
            if tid not in tables:
                tables[tid] = {food : 1}
            else:
                tables[tid][food] = tables[tid].get(food, 0) + 1
        res = [["Table"]]
        for f in sorted(foods):
            res[0].append(f)
        for k, v in sorted(tables.items()):
            tmp = [str(k)]
            i = 1
            while i < len(res[0]):
                if res[0][i] in v:
                    tmp.append(str(v[res[0][i]]))
                else:
                    tmp.append('0')
                i += 1
            res.append(tmp)
        return res

test = Solution()
print test.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])
print test.displayTable([["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]])
print test.displayTable([["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]])