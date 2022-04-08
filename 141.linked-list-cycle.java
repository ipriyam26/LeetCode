/*
 * @lc app=leetcode id=141 lang=java
 *
 * [141] Linked List Cycle
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
       ListNode fast = head;
       ListNode slow = head;

       while(fast!=null && fast.next!=null){
           
        //    try {
            fast= fast.next.next;

        //    } catch (Exception e) {
        // return false;   
        // }
           slow=slow.next;
           if(fast==slow){
               return true;
           }
       }
       return false;
        
    }
}
// @lc code=end

