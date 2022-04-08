import java.util.Arrays;
import java.util.Map;

/*
 * @lc app=leetcode id=853 lang=java
 *
 * [853] Car Fleet
 */

// @lc code=start
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
       Map<Integer,Integer> store =  new HashMap<Integer,Integer>();
       for (int i = 0; i < speed.length; i++) {
           store.put(position[i], speed[i]);
       } 

       int i=speed.length-1;
       for (Map.Entry<Integer, Integer> entry : store.entrySet()) {
           speed[i]= entry.getValue();
           i--;
       }
// System.out.println(Arrays.toString(speed));
       
       return dips;
       
    }
}
// @lc code=end

