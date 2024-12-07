class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(set)
        self.post_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].add((self.post_time, tweetId))
        self.post_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news = self.posts[userId].copy()
        for followee in self.follows[userId]:
            news.update(self.posts[followee])
        news = sorted(list(news), reverse=True)[:10]
        news = list(map(lambda x:x[1], news))
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# This is probably better if most people are connected, otherwise the first solution is probably better.
# Imagine iterating through every tweet existing for every user, then check if it is relevant
class Twitter:

    def __init__(self):
        self.tweets = []
        self.network = set()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int):
        count = 0
        relevant = []
        for i in range(len(self.tweets) - 1, -1, -1):
            poster, post = self.tweets[i]
            if (userId, poster) in self.network or userId == poster:
                count += 1
                relevant.append(post)
            if count == 10:
                break
        return relevant

    def follow(self, followerId: int, followeeId: int) -> None:
        self.network.add((followerId, followeeId))

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId, followeeId) in self.network:
            self.network.remove((followerId, followeeId))


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,5)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.follow(1,2)
obj.postTweet(2,6)
param_2 = obj.getNewsFeed(1)
print(param_2)
