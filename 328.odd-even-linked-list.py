#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        head_odd = head
        head_even = head.next
        odd,even = head_odd,head_even
        while even.next:
            odd.next = even.next
            odd= odd.next

            if not odd.next:
                break
            even.next = odd.next
            even =even.next

        even.next = None
        odd.next = head_even

        return head_odd
            
        
        
        
        
# @lc code=end

