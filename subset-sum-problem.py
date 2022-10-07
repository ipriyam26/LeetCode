#User function Template for python3

import itertools
from typing import List


class Solution:

    
    def subset_sum(self,sum_needed,n,wt):
        dp= [[None for _ in range(sum_needed+1)] for _ in range(n+1)]

        for i in range(sum_needed+1):
            dp[0][i]=False
        for i in range(n+1):
            dp[i][0]=True

        for i, j in itertools.product(range(1,n+1), range(1,sum_needed+1)):
            dp[i][j] = dp[i-1][j] if j > wt[i-1] else dp[i-1][j] or dp[i-1][j-wt[i-1]]
            
        return dp[i][j]

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        sum_needed= int(input())
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.launch(sum_needed=sum_needed,n=len(wt),wt=wt))
# } Driver Code Ends