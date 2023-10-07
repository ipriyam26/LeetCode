from typing import List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A:List[int], B:int):
        table = {0:1}
        count =0
        xor = 0
        for num in A:
            xor = xor^num
            search = xor^B
            if search in table:
                count+= table[search]
            if xor in table:
                table[xor]+=1
            else:
                table[xor]=1
        return count
print(Solution().solve([5, 6, 7, 8, 9],5))
            
        
