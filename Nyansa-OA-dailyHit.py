import datetime
class Solution(object):
    def dailyHit(self, input):
        dic = {}
        for row in input:
            row = row.split('|')
            date = datetime.datetime.fromtimestamp(int(row[0])).strftime('%m/%d/%Y')
            if date in dic:
                dic[date].append(row[1])
            else:
                dic[date] = [row[1]]

        for key in sorted(dic):
            tmp = {}
            for site in dic[key]:
                tmp[site] = tmp.get(site, 0) + 1
            print key
            for key, val in tmp.items():
                print key + ' ' + str(val)

test = Solution()
print test.dailyHit(['1407564301|www.nba.com', '1407478021|www.facebook.com', '1407478023|www.leetcode.com', '1407478022|www.facebook.com', '1407648022|www.twitter.com'])