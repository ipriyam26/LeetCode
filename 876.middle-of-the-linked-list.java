/*
 * @lc app=leetcode id=876 lang=java
 *
 * [876] Middle of the Linked List
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
    public ListNode middleNode(ListNode head) {

        // int mid = lengthOfLinkedList(head)/2;
        

//         while(mid>0){
//             head= head.next;
//             mid--;

//         }
// return head;
ListNode fast = head;
ListNode slow = head;
while(fast!=null && fast.next != null){
    fast=fast.next.next;
    slow = slow.next;

}
return slow;

        
    }
    
}
// @lc code=end

