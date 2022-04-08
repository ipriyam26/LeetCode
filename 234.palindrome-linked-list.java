import java.util.Stack;

/*
 * @lc app=leetcode id=234 lang=java
 *
 * [234] Palindrome Linked List
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
    int sum=0;

    public boolean isPalindrome(ListNode head) {



        
    }
    public ListNode middleFinder(ListNode head){

        ListNode fast = head;
        ListNode slow = head;
        Stack<Integer> palindrome = new Stack<Integer>();
int i =1;

while (fast != null && fast.next != null) {
    fast = fast.next.next;
    slow = slow.next;
}
if (fast != null) { // odd nodes: let right half smaller
    slow = slow.next;
}


    



    }
}
// @lc code=end

