from collections import OrderedDict
class TweetCounts(object):
    def __init__(self):
        self.second = {}

    def recordTweet(self, tweetName, time):
        if tweetName in self.second:
            self.second[tweetName][time] = self.second[tweetName].get(time, 0) + 1
        else:
            self.second[tweetName] = OrderedDict()
            self.second[tweetName][time] = 1

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        res = []
        dic = OrderedDict()
        if tweetName not in self.second:
            return []
        else:
            counts = OrderedDict()
            for i in range(startTime, endTime + 1):
                if i not in self.second[tweetName]:
                    continue
                else:
                    counts[i] = self.second[tweetName][i]
            if freq == "minute":
                for k, v in counts.items():
                    m = k / 60
                    dic[m] = dic.get(m, 0) + v
                for v in dic.values():
                    res.append(v)
            elif freq == "hour":
                for k, v in counts.items():
                    h = k / 3600
                    dic[h] = dic.get(h, 0) + v
                for v in dic.values():
                    res.append(v)
            elif freq == "day":
                for k, v in counts.items():
                    d = k / 86400
                    dic[d] = dic.get(d, 0) + v
                for v in dic.values():
                    res.append(v)

            return res

test = TweetCounts()
test.recordTweet("tweet3", 0)
test.recordTweet("tweet3", 60)
test.recordTweet("tweet3", 10)
print test.getTweetCountsPerFrequency("minute", "tweet3", 0, 59)
print test.getTweetCountsPerFrequency("minute", "tweet3", 0, 60)
test.recordTweet("tweet3", 120)
print test.getTweetCountsPerFrequency("hour", "tweet3", 0, 210)