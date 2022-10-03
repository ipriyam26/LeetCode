#User function Template for python3

from collections import defaultdict



class Solution:

    def default_value(self):
        return 0
        
    
    def longestKSubstr(self, s, k):
        holder = defaultdict(self.default_value)
        unique_count = 0
        max_count = 0
        max_string=0
        i,j=0,0
        while j <len(s):
            holder[s[j]]+=1
            unique_count =j-i+1
            if (len(holder)<k):
                pass
            elif (len(holder)==k):
                if unique_count >max_count:
                    max_count = unique_count
                    max_string = s[i:j+1]
            else:
                #remove elements till unique are 3
                while len(holder)>k and i<j:
                    holder[s[i]]-=1
                    if(holder[s[i]]==0):
                        holder.pop(s[i])
                    i+=1

            j+=1
        # print(max_string)
        # print(i,j)
        return max_count or -1
            
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