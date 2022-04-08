import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * @lc app=leetcode id=39 lang=java
 *
 * [39] Combination Sum
 */

// @lc code=start
class Solution {

    List<Integer> current;
    List<List<Integer>> result;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {

        Arrays.sort(candidates);
         current = new ArrayList<Integer>();
         result = new ArrayList<List<Integer>>();
        backtrack(result, current, candidates, target, 0);
        return result;
        
    }
    public static void backtrack(List<List<Integer>> result, List<Integer> current,int[] candidates, int target, int start){

        if(target>0){
         
            for (int i = start; i <candidates.length && target>=candidates[i] ; i++) {
                current.add(candidates[i]);
                // the current change will be marked in and kept until it fails and gets popped, i.e it gets returned
                backtrack(result, current, candidates, target-candidates[i], i);
                // will only run if the case fails
                current.remove(current.size()-1);
            }

        }

        else if(target==0) {
            // If all goes well this will add the current list to the answere list 
            result.add(current);
        }
        else{
            // this is for the case where the resulting target becomes smaller than zero so the case fails and list element must be popped out
            return;
        }


    }
}
// @lc code=end

