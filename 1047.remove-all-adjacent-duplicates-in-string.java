import java.util.Stack;

/*
 * @lc app=leetcode id=1047 lang=java
 *
 * [1047] Remove All Adjacent Duplicates In String
 */

// @lc code=start
class Solution {

    // Copied this one from the solutions redo it again
    public String removeDuplicates(String s) {
        char[] arr = s.toCharArray();
        int start = 0;
        for (int end = 0; end < arr.length; end++) {
            arr[start] = arr[end];
            if (start > 0) {
                if (arr[start] == arr[start - 1]) {
                    start -= 2;
                }
            }
            start++;
        }
        return new String(arr, 0, start);
    }
}
// @lc code=end

// class Solution {
//     public String removeDuplicates(String s) {
//        // 每次遍历都将原字符串存入答案字符串，如果发现有两个连续的元素相等则指针退回两位，遍历结束后直接返回一个子字符串就是答案。 
//         char[] chars = s.toCharArray();
//         int start = 0;
//         for (int end = 0; end < chars.length; end++) {
//             chars[start] = chars[end];
//             if (start > 0 && chars[start] == chars[start - 1]) {//count = 2
//                 start -= 2;
//             }
//             start++;
//         }
//         return new String(chars, 0, start);
//     }