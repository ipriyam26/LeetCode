#User function Template for python3
import itertools


class Solution:
    def minOperations(self, s1, s2):
        return len(s1)+len(s2)-2*self.longestCommonSubsequence(s1,s2)
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text2)
        n = len(text1)
        self.dp = [[ 0 for _ in range(m+1)] for _ in range(n+1)]
        i,j=0,0
        for i, j in itertools.product(range(1,n+1), range(1,m+1)):
            if text1[i-1] == text2[j-1]:
                self.dp[i][j] = self.dp[i - 1][j - 1] +1 
            else:
                self.dp[i][j]=max(self.dp[i - 1][j], self.dp[i][j - 1])

        return self.dp[n][m]
    

     
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends