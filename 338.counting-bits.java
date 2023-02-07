/*
 * @lc app=leetcode id=338 lang=java
 *
 * [338] Counting Bits
 */

// @lc code=start
class Solution {

  public int[] countBits(int n) {
    int[] result = new int[n + 1];
    int currentTotalBits = 1;
    int currentSet = 0;
    int toBeSet = 0;
    for (int i = 0; i < result.length; i++) {
      result[i] = currentSet;
      if (currentSet < currentTotalBits) {
        currentSet += 1;
      } else {
        currentTotalBits += 1;
        currentSet = 1;
      }
    }
    return result;
  }
}
// @lc code=end
