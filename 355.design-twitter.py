#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
class Twitter:

    def __init__(self):
        #{'userID':followed}
        self.followed = {}
        self.tweets = {}
        
        

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets.keys():
            self.tweets[userId].append(tweetId)
        else:
            self.tweets[userId] = [tweetId]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

