# -*- coding: utf-8 -*-
class Solution(object):
    def lunchRecommandation(self, menu, person):
        dicm = {}
        dicp = {}
        tmp = set()
        res = []

        # Italian => Pizza
        for item in menu:
            food = item[0]
            style = item[1]
            if style in dicm:
                dicm[style].append(food)
            else:
                dicm[style] = [food]

        # Peter => Italian
        for elem in person:
            name = elem[0]
            style = elem[1]
            if name in dicp:
                dicp[name].append(style)
            else:
                dicp[name] = [style]

        # [Peter, Pizza]
        for key, val in dicp.items():
            for style in val:
                if style == "＊":
                    for item in menu:
                        tmp.add((key, item[0]))
                    continue
                if style in dicm:
                    for food in dicm[style]:
                        tmp.add((key, food))

        # convert set tuple into list
        for t in tmp:
            res.append(list(t))

        return res


test1 = Solution()
print test1.lunchRecommandation([["Pizza", "Italian"], ["Pasta", "Italian"], ["Burger", "American"]], [["Peter", "Italian"], ["Adam", "American"], ["Peter", "＊"]])