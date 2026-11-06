from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq

        heap = []

        for user in self.following[userId] | {userId}:
            if self.tweets[user]:
                i = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][i]
                heapq.heappush(heap, (-time, tweetId, user, i))

        result = []

        while heap and len(result) < 10:
            time, tweetId, user, i = heapq.heappop(heap)
            result.append(tweetId)

            if i > 0:
                new_time, new_tweetId = self.tweets[user][i - 1]
                heapq.heappush(heap, (-new_time, new_tweetId, user, i - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)