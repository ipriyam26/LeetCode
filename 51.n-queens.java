import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode id=51 lang=java
 *
 * [51] N-Queens
 */

// @lc code=start
class Solution {

    public boolean isSafe(List<List<String>> board,int row,int col ){

        // checking the column for any Q

        for (int i = 0; i < board.size(); i++) {
            
            if(board.get(i).get(col)=="Q"){
                return false ;
            }}

        // checking the diagonal from that row
        for (int i = row, j=col; j >=0 && i>=0; j--,i--) {
            if(board.get(i).get(j)=="Q"){
                return false;
            }
        }
                // checking the diagonal from that row
        for (int i = row, j=col; j <board.size() && j<board.size(); j++,i++) {
            if(board.get(i).get(j)=="Q"){
                return false;
            }
        }

        return true;
            

    }


    public List<List<String>> solveNQueens(int n) {
        List<List<String>> board = new ArrayList<List<String>>();

        for (int i = 0; i < board.size(); i++) {
            List
            for (int j = 0; j < board.size(); j++) {
                
            }
            
        }
    }
}
// @lc code=end

