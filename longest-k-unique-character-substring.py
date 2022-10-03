#User function Template for python3

from collections import defaultdict



class Solution:

    def longestKSubstr(self, s, k):
        holder = defaultdict()
        unique_count = 0
        max_count = 0
        i,j=0,0
        while j <len(s):
            holder[s[j]]+=1
            unique_count =j-i
            if(len(holder)<k):
                j+=1
            elif (len(holder)==k):
                if unique_count >max_count:
                    max_count = unique_count
                j+=1
            else:
                #remove elements till unique are 3
                
            
                
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends