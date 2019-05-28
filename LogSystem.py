# LC-635
class LogSystem(object):
    def __init__(self):
        self.dic = {}
        self.gras = ["Year", "Month", "Day", "Hour", "Minute"]

    def put(self, id, timestamp):
        self.dic[timestamp] = id

    def getKeyByGra(self, timestamp, gra):
        t = timestamp.split(":")
        for i in range(len(self.gras)):
            if gra == self.gras[i]:
                tmp = []
                for _ in range(len(t) - i - 1):
                    tmp.append("00")
                return ''.join(t[:i + 1]) + ''.join(tmp)

    def retrieve(self, s, e, gra):
        res = []
        sGra = self.getKeyByGra(s, gra)
        eGra = self.getKeyByGra(e, gra)
        for k in self.dic.keys():
            kGra = self.getKeyByGra(k, gra)
            if sGra <= kGra <= eGra:
                res.append(self.dic[k])
        return res

test = LogSystem()
test.put(1, "2017:01:01:23:59:59")
test.put(2, "2017:01:01:22:59:59")
test.put(3, "2016:01:01:00:00:00")
print test.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year")