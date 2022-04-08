import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/*
 * @lc app=leetcode id=739 lang=java
 *
 * [739] Daily Temperatures
 */

// @lc code=start
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        if (temperatures.length == 0 || temperatures.length == 1) {
            return temperatures;
        }
        Stack<Integer> value = new Stack<Integer>();
        Stack<Integer> index = new Stack<Integer>();
        int[] answerer = new int[temperatures.length];
        int i = 0;
        while (i < temperatures.length) {
            if (value.isEmpty()) {
                value.add(temperatures[i]);
                index.add(i);
                i++;
                continue;
            }

            while (temperatures[i] > value.peek()) {
                answerer[index.peek()] = i - index.peek();
                value.pop();
                index.pop();
                if (value.isEmpty()) {
                    break;
                }
            }
            value.push(temperatures[i]);
            index.push(i);
            i++;
        }
        while (!value.isEmpty()) {
            answerer[index.pop()] = 0;
            value.pop();
        }
        return answerer;

    }
}
// @lc code=end
