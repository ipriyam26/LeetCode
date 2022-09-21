#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
from collections import defaultdict

from typing import Dict, List


class Twitter:

    def __init__(self):
        #{'userID':followed}
        self.follow_list :Dict[int,List[int]]= defaultdict(list)
        self.tweets:Dict[int,List[int]] = defaultdict(list)
        
        

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(tweetId)

    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_list[followeeId]:
            self.follow_list[followeeId].append(followerId)
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        valid_tweets = []
        following_list = self.follow_list[userId]
        following_list.append(userId)
        for followers in following_list:
            valid_tweets.extend(self.tweets[followers])
        
        
        

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

