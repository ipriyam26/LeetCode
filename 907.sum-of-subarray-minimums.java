import java.lang.reflect.Array;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Stack;

/*
 * @lc app=leetcode id=907 lang=java
 *
 * [907] Sum of Subarray Minimums
 */

// @lc code=start
class Solution {

    public int sum(int[] arr){
        int sum=0;
        for (int i : arr) {
            sum+=i;
        }
        return sum;
    }
    public int sumSubarrayMins(int[] arr) {

        int sum = sum(arr);
        int i=0;
       Deque<Integer> holder = new LinkedList<Integer>();
        while (i<arr.length-1) {
            int temp = Math.min(arr[i], arr[i+1]);
            sum+=temp;
            holder.push(temp);
            i++;
        }
int turn=1;
        while (!holder.isEmpty()) {
            int cc=0;
            while (cc<i-turn) {
                int first=holder.removeFirst();
                int smaller =Math.min(first , holder.getFirst());
                sum+=smaller;
                holder.addLast(smaller);
            }
            holder.removeFirst();
            turn++;
            
        
            
        }
        return sum;



    }

}
// @lc code=end

