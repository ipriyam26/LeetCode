import java.util.Arrays;
import java.util.Map;

/*
 * @lc app=leetcode id=853 lang=java
 *
 * [853] Car Fleet
 */

// @lc code=start
class Solution {

  public int carFleet(int target, int[] pos, int[] speed) {
    int N = pos.length, res = 0;
    double[][] cars = new double[N][2];
    for (int i = 0; i < N; ++i)
        cars[i] = new double[] {pos[i], (double)(target - pos[i]) / speed[i]};
    Arrays.sort(cars, (a, b) -> Double.compare(a[0], b[0]));
    double cur = 0;
    for (int i = N - 1; i >= 0 ; --i) {
        if (cars[i][1] > cur) {
            cur = cars[i][1];
            res++;
        }
    }
    return res;
  }


}
// @lc code=end
