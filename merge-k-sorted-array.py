#User function Template for python3

from typing import List


class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr: List[List[int]], K):
        array = []
        for array in arr:
            for element in array:
                array.append(element)
                
                
        # code here
        # return merged list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        ob = Solution();
        merged_list=ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()
# } Driver Code Ends