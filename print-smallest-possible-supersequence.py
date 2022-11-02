import itertools 
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        lcs = self.make_substring(str1,str2)
        k,i,j=0,0,0
        n,m = len(str1),len(str2)
        len_lcs = len(lcs)
        result = ""
        while k<len_lcs:
            while i<n and str1[i]!=lcs[k]  :
                result+=str1[i]
                i+=1
            while j<m and str2[j]!=lcs[k]  :
                result+=str2[j]
                j+=1
            result +=lcs[k]
            k+=1
            i+=1
            j+=1
        if i < n:
            result+=str1[i:]
        if j<m:
            result+=str2[j:]
        
        return result
            
                       
                
            
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
    

    
    def make_substring(self,text1:str,text2:str):
        self.longestCommonSubsequence(text1=text1,text2=text2)
        result = ""
        j,i = len(text2),len(text1)
        while i >0 and j>0:
            if text1[i-1]==text2[j-1]:
                result=text1[i-1]+result
                i-=1
                j-=1
            elif self.dp[i-1][j]>self.dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        # result = result[::-1]
        return result

if __name__=="__main__":
    str1 = "aaaaaaaa"
    str2 = "aaaaaaaa"
    sol = Solution()
    print(sol.shortestCommonSupersequence(str1,str2))