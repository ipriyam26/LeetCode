import java.util.Stack;

/*
 * @lc app=leetcode id=581 lang=java
 *
 * [581] Shortest Unsorted Continuous Subarray
 */

// @lc code=start
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int i = 0;

        Stack<Integer> shortestUnsortedSubarray = new Stack<Integer>();
        if (nums.length == 1) {
            return 0;
        } else if (nums.length == 2) {
            return nums[0] < nums[1] ? 0 : 2;
        }


        while (nums[i + 1] >= nums[i]) {
            i++;
            if (i == nums.length - 2) {
                i=nums.length-1;
                break;
            }
        }

        while (i < nums.length) {

            shortestUnsortedSubarray.push(nums[i]);
            i++;

        }

        while (!shortestUnsortedSubarray.isEmpty()) {
            int last_hold = shortestUnsortedSubarray.pop();
            int previous_hold = shortestUnsortedSubarray.peek();
            System.out.println("Comparing" + last_hold + "<->" + previous_hold);
            if (last_hold < previous_hold) {
                shortestUnsortedSubarray.push(last_hold);
                break;
            }
        }

        int lengthShortestSubarray = 0;
        while (!shortestUnsortedSubarray.isEmpty()) {
            lengthShortestSubarray++;
            // System.out.print(shortestUnsortedSubarray.pop() +" ");

        }
        return lengthShortestSubarray;
    }
}
// @lc code=end
