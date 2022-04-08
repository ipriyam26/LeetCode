/*
 * @lc app=leetcode id=25 lang=java
 *
 * [25] Reverse Nodes in k-Group
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {

        if(head==null || head.next==null){
            return head;
        }

        ListNode prev=null;
        ListNode curr = head;
        ListNode next = curr.next;
        ListNode newStart = null;

        int f=0;
        while(curr!=null){

            ListNode newHead = curr;
            for (int i = 0; i < k; i++) {

                curr.next = prev;
                prev = curr;
                curr = next;
                if(next.next!=null){
                    next = next.next;
                }                
                
            }
            if(f==0){

                newStart = prev;
                f=1;
            }

            newHead.next = curr;
            curr = next;
            if(next.next!=null){
                next = next.next;
            }


        }
return newStart;
    }
}
// @lc code=end

