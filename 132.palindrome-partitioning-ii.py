#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
import sys

class Solution:
  
    
    def minCut(self, s):
        if not s or len(s) <=1:
            return 0

        elif self.is_palindrome(s):
            return 0

        rows = len(s)
        cols = len(s)

        # Optimization 1(Major) aka Memoization of results(Top Down DP)
        dp = [[-1]*cols for _ in range(rows)]

        # Optimization 2(Minor) aka Memoization of palindrome check results
		# This optimization wont solve your TLE error on LC but still is a good optimization
        p_cache = {} # dictionary/map

        return self.min_cuts_recursively_mcm(0, len(s)-1, s, dp, p_cache)
    
    def is_palindrome(self, t):
        return t == t[::-1]
        
    def min_cuts_recursively_mcm(self, i, j, s, dp, p_cache):
	
        # base case
        if i >= j:
            return 0
        
        # if computation has already been done
        elif dp[i][j] != -1:
            return dp[i][j] 
        
        # if the string has already been checked for palindrome in past
        elif p_cache.get((i,j)):
            return 0 # since, its palindrome, ZERO cuts required
        
        # if not checked for palindrome, check it
        elif self.is_palindrome(s[i:j+1]):
            
            # store it
            p_cache[(i,j)] = True
            return 0 # since, its palindrome, ZERO cuts required
        
        curr_min = sys.maxsize
        for k in range(i,j):
            
            # IMP Optimization 3 (Major) this will solve your TLE on Leetcode or other platform
            # Why to check further if the left part of the cut ie. S[i,k+1] is itself NOT a palindrome ??????
            # the right part anyhow wont be able to contribute to the answer
            if self.is_palindrome(s[i:k+1]): # we only move forward with the cut if the left part is sure shot a palindrome, TLE FIXED
                left_result = 0
                right_result = self.min_cuts_recursively_mcm(k+1, j, s, dp, p_cache)
                curr_min = min(curr_min, (left_result+right_result+1))
                dp[i][j] = curr_min
        
        return curr_min

        
# @lc code=end

