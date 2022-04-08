// @before-stub-for-debug-begin

// @before-stub-for-debug-end

/*
 * @lc app=leetcode id=83 lang=cpp
 *
 * [83] Remove Duplicates from Sorted List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *deleteDuplicates(ListNode *head)
    {
        ListNode *cur_node = head;
        while (cur_node && cur_node->next)
        {
            ListNode *next_node = cur_node->next;
            if (cur_node->val == next_node->val)
            {
                cur_node->next = next_node->next;
            }
            else
            {
                cur_node = next_node;
            }
        }
        return head;
    }
};
// @lc code=end
