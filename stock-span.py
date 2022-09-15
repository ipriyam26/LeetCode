#User function Template for python3


class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        res = []
        stack = []
        for i in range(n):
            if not stack:
                res.append(1)
            elif stack[-1][0] >= a[i]:
                res.append(i-stack[-1][1])
            else:
                while stack and stack[-1][0]<a[i]:
                    stack.pop()
                if not stack:
                    res.append(i)
                res.append(i-stack[-1][1])
            stack.append(a[i],i)
        return res
        

















#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n);
        for i in range(n):
            print(ans[i],end=" ")
        print()            
# } Driver Code Ends