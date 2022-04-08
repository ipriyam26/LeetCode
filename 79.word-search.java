/*
 * @lc app=leetcode id=79 lang=java
 *
 * [79] Word Search
 */

// @lc code=start
class Solution {
    public boolean exist(char[][] board, String word) {

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if(board[i][j]==word.charAt(0)){
                    if(backtrack(board, i, j, word)){
                        return true;
                    }
                }
            }
        }
        return false;
        
    }

    public boolean backtrack(char[][] board,int i,int j, String word){
        // This function will return true only if the word is empty as we are removing the first element of the word each time we find a match
        // hence if all the digits are found it must be empty
        if(word==""){
            return true;
        }
        // runs when there are still char left in the word to find
        else{
// Checks if the current first char of word matches with the current position on the board
// also does a check for 1 that is we are marking the places we have already been to as 1 so if comes again it is not acceptable and backtrack
        if(board[i][j] == word.charAt(0) && board[i][j]!='1'){
            // Marking our presence by changing this postion on the board to be 1 
            board[i][j]='1';
            // Checks whether it is possible to goto below
            if(i<board.length-1 ){

               if(backtrack(board, i+1, j, word.substring(1))){
                   return true;
               }

            }

             if(i>1){
                if(backtrack(board, i-1, j, word) ){
                    return true;
                }
            }
            if(j<board.length-1 ){

               if(backtrack(board, i, j+1, word.substring(1))){
                   return true;
               }
            }
            if(j>1){
                if(backtrack(board, i, j-1, word) ){
                    return true;
                }
            } 
            // Changes is back to original as its going to return false and do back from this selection 
            board[i][j] = word.charAt(0);
        }
            // is it doesn't match the required char at this position move out and back

        return false;
 
        }

   }
}
// @lc code=end

