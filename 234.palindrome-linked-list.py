#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        stack = []
        while head:
            if stack and stack[-1] == head.val:
                stack.pop()
            else:
                stack.append(head.val)
            head = head.next
        print(stack)
        return not stack
        
# @lc code=end

