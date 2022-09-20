#User function Template for python3

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def cutRod(self, price:List[int], n):
        heapify(price)
        cost = 0
        while len(price)>1:
            pooped = heappop(price)
            cost+=pooped
            heappush(price,cost)
        cost+=price[0] 
        print(cost)
            
        #code here
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends