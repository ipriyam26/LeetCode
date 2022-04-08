/*
 * @lc app=leetcode id=142 lang=java
 *
 * [142] Linked List Cycle II
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
    public ListNode detectCycle(ListNode head){

int length = lengthCycle(head);
if(length==0){
    return null;

}
ListNode ptr1 = head;
ListNode ptr2 = head;
while(length>0){
    ptr2=ptr2.next;
length--;
}
while(ptr1!=ptr2){
    ptr1=ptr1.next;
    ptr2=ptr2.next;
}
return ptr1;



    } 
    public int lengthCycle(ListNode head)
{
       ListNode fast = head; 
       ListNode slow = head; 
       int length = 0;
       while(fast!=null && fast.next!=null){
        fast = fast.next.next;
        slow = slow.next;
        if(fast==slow){
            ListNode temp = slow;
            do{
                temp=temp.next;
                length++;
                
            }while(temp!=slow);
            return length;
        }

       }
       return 0;
    
    }
}
// @lc code=end

