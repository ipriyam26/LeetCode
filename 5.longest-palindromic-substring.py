#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def make_sub(self, s1: str, i: int, j: int):
        if i == len(s1) or j == -1:
            return ""
        if s1[i] == s1[j]:
            # meaning they both are same
            # so now subtract from both of them
            return s1[i] + self.make_sub(s1, i + 1, j - 1)
        # they are not equal so return of check for both
        r1 = self.make_sub(s1, i + 1, j)
        r2 = self.make_sub(s1, i, j - 1)
        return r1 if len(r1) > len(r2) else r2

    def longestPalindrome(self, s: str) -> str:
        return self.make_sub(s1=s,i=0,j=len(s)-1)

if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
# @lc code=end
