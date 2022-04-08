import java.util.Deque;
import java.util.LinkedList;


/*
 * @lc app=leetcode id=143 lang=java
 *
 * [143] Reorder List
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
    public void reorderList(ListNode head) {

       Deque<ListNode> q = new LinkedList<ListNode>();
        if(head==null || head.next==null){
            return;
        }
       ListNode temp = head;
      while (temp!=null) {
          q.add(temp);
          temp = temp.next;
      }

      ListNode temp2 = new ListNode();
      head = temp2;
      while (q.size()!=0) 
      {
          temp2.next = q.removeFirst();
          temp2 = temp2.next;
          if(q.size()!=0){

              temp2.next = q.removeLast();
              temp2 = temp2.next;
          }
          temp2.next = null;
      }

    head = head.next;

    // head = temp2.next;
    // while (head!=null) {
    //     System.out.println(head.val);
    //     head = head.next;
    // }
       

    }
}
// @lc code=end

