#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.toBST(head, None) if head else None
    def toBST(self,head,tail):
        slow = head
        fast = head
        if head == tail: return None
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        
        root = TreeNode(val=slow.val)
        root.left = self.toBST(head,slow)
        root.right = self.toBST(slow.next,tail)
        return root
        
        

        
# @lc code=end

