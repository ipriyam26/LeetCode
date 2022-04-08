
/*
 * @lc app=leetcode id=61 lang=java
 *
 * [61] Rotate List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {

        if (k<=0|| head == null || head.next == null) {
            return head;
        }
        int i = 0;

        int len = 1;
        ListNode temp = head;
        while (temp.next != null) {
            len++;
            temp = temp.next;
        }
        // System.out.println(len);
        
        k = k % len;
        if (k <= 0) {
            return head;
        }
        // System.out.println(len - k);

        i = 1;
        ListNode prevLast = head;
        while (i < len - k) {

            prevLast = prevLast.next;
            i++;

        }
        ListNode newHead = prevLast.next;
        prevLast.next = null;
        temp.next = head;

//         while(head!=null){
// System.out.println(head.val);
// head=head.next;
//         }

        return newHead;

    }

}
// @lc code=end
