from collections import defaultdict

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = []  # chronological tweets
        self.following = defaultdict(list)

    def postTweet(self, userId, tweetId):
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId):
        followers = [userId]
        followers += self.following[userId]

        tweets = []
        for userId, tweetId in reversed(self.tweets):
            if userId in followers:
                tweets.append(tweetId)
            if len(tweets) == 10:
                break

        return tweets

    def follow(self, followerId, followeeId):
        self.following[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


