#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
from collections import defaultdict
import heapq

from typing import Dict, List


class Twitter:

    def __init__(self):
        #{'userID':followed}
        self.follow_list :Dict[int,List[int]]= defaultdict(list)
        self.tweets:Dict[int,List[int]] = defaultdict(list)
        self.time = 0
        
        

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1

    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_list[followerId]:
            self.follow_list[followerId].append(followeeId)
        self.time+=1
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        valid_tweets = []
        following_list=[]
        following_list = self.follow_list[userId].copy()
        following_list.append(userId)
        print(f"Original temp {self.follow_list[userId]}")
        print(f"Following {following_list} for {userId}")
        for followers in following_list:
            valid_tweets.extend(self.tweets[followers])
        min_heap = []
        for tweet in valid_tweets:
            heapq.heappush(min_heap,tweet)
            if len(min_heap)>10:
                heapq.heappop(min_heap)
            print(min_heap)
            
        ans = []
        while min_heap:
            pooped = heapq.heappop(min_heap)
            ans.index(0,pooped[1])
        self.time+=1
        return min_heap
    
        
        
        
        

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_list[followerId]:
            self.follow_list[followerId].remove(followeeId)
        self.time+=1
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

