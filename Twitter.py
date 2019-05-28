import heapq
class Twitter(object):
    def __init__(self):
        self.timer = 0
        # uid => (time, tweetID)
        self.tweets = {}
        # followerID => [followeeId]
        self.friends = {}

    def postTweet(self, userId, tweetId):
        if userId not in self.tweets:
            self.tweets[userId] = [(self.timer, tweetId)]
        else:
            self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1


    def getNewsFeed(self, userId):
        feedheap = []
        feedlist = []
        heapq.heapify(feedheap)
        for tweet in self.tweets[userId]:
            heapq.heappush(feedheap, tweet)
        for followee in self.friends[userId]:
            for tweet in self.tweets[followee]:
                heapq.heappush(feedheap, tweet)

        while len(feedheap) > 10:
            heapq.heappop(feedheap)

        for t, v in feedheap:
            feedlist.append(v)

        return feedlist


    def follow(self, followerId, followeeId):
        if followerId not in self.friends:
            self.friends[followerId] = [followeeId]
        else:
            if followeeId not in self.friends[followerId]:
                self.friends[followerId].append(followeeId)


    def unfollow(self, followerId, followeeId):
        if followerId not in self.friends:
            return False
        else:
            if followeeId in self.friends[followerId]:
                self.friends[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
obj.postTweet(2, 6)
obj.postTweet(2, 7)
obj.follow(1, 2)
print obj.getNewsFeed(1)
