#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        holder = []
        for i,node in enumerate(lists):
            heappush(holder,(node.val,i,node))
        head = ListNode()
        temp = head   
        while holder:
            pooped = heappop(holder)
            temp.next = pooped[2]
            temp=temp.next
            if temp.next:
                heappush(holder,(temp.next.val,pooped[1],temp.next))
        return head.next
            
            
            
        
# @lc code=end

