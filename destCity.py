class Solution(object):
    def destCity(self, paths):
        outgoing = set()
        for p in paths:
            outgoing.add(p[0])
        for p in paths:
            if p[1] not in outgoing:
                return p[1]
        return -1