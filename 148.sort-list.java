/*
 * @lc app=leetcode id=148 lang=java
 *
 * [148] Sort List
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


    // public ListNode sortList(ListNode head) {
    //     if (head == null || head.next == null) {
    //         return head;
    //     }

    //     ListNode mid = getMid(head);
    //     ListNode left = sortList(head);
    //     ListNode right = sortList(mid);

    //     return merge(left, right);
    // }

    // ListNode merge(ListNode list1, ListNode list2) {
    //     ListNode dummyHead = new ListNode();
    //     ListNode tail = dummyHead;
    //     while (list1 != null && list2 != null) {
    //         if (list1.val < list2.val) {
    //             tail.next = list1;
    //             list1 = list1.next;
    //             tail = tail.next;
    //         } else {
    //             tail.next = list2;
    //             list2 = list2.next;
    //             tail = tail.next;
    //         }
    //     }
    //     tail.next = (list1 != null) ? list1 : list2;
    //     return dummyHead.next;
    // }

    // ListNode getMid(ListNode head) {
    //     ListNode midPrev = null;
    //     while (head != null && head.next != null) {
    //         midPrev = (midPrev == null) ? head : midPrev.next;
    //         head = head.next.next;
    //     }
    //     ListNode mid = midPrev.next;
    //     midPrev.next = null;
    //     return mid;
    // }









//<---------------------------------------------------------->

    public ListNode sortList(ListNode head) {
        if (head==null || head.next==null){
            return head;
        }
        ListNode mid = middleNode(head);
        ListNode firstHalf = sortList(head);
        ListNode secondhalf = sortList(mid);
        return mergeTwoLists(firstHalf, secondhalf);
        
    }


    public ListNode middleNode(ListNode head) {

        ListNode midPrev = null;

        while(head!=null && head.next != null){
    midPrev = (midPrev==null)?head:midPrev.next;
    head = head.next.next;
}
ListNode mid = midPrev.next;
midPrev.next = null;
return mid;
    }




    
    public ListNode mergeTwoLists(ListNode head,ListNode head2)    {

        // ListNode ptr = head;
        // ListNode ptr2 = head2;
        ListNode tempHead = new ListNode();
        ListNode ptr = tempHead;

        while(head!=null && head2 !=null)
        {
            if(head.val<head2.val){
        ptr.next = head;
        head=head.next;
        ptr = ptr.next;

            }
            else{
                ptr.next = head2;
                head2 = head2.next;
                ptr=ptr.next;
            }
            // 
            
        }
        ptr.next = (head!=null)? head:head2;
        return tempHead.next;
    }
}
// @lc code=end

