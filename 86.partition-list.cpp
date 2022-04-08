/*
 * @lc app=leetcode id=86 lang=cpp
 *
 * [86] Partition List
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
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *headS = new ListNode();
        ListNode *smaller = headS;
        ListNode *headB = new ListNode();
        ListNode *bigger = headB;
        while (head)
        {
            if(head->val < x){
                smaller->next = head;
                smaller=smaller->next;
            }
            else
            {
                bigger->next = head;
                bigger = bigger->next;
            }
            head=head->next;
            
        }
        bigger->next=NULL;
        smaller->next = headB->next;
        return headS->next;
    }
};
// @lc code=end

